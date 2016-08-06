from django.shortcuts import render, get_object_or_404
from app.models import Company, Promotion, Visit, Guest, PromoCode
from api.vk import VKApi
from api.ok import Odnoklassniki, OdnoklassnikiError
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth import logout
from .forms import UserDataForm
from django.views.generic import View

class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html', {})

class PromocodeView(View):
    def get(self, request):
        code = PromoCode.promo_gen()
        return HttpResponse(code)

    def post(self, request):
        guest = Guest.objects.filter(pk=request.POST['guest']).first()
        if guest:
            promo_code = PromoCode.create(guest,request.POST['promo_code'])
            promo_code.save()
            return HttpResponse('done');

class PromotionView(View):
    form_class = UserDataForm
    company_info = {
        "company_id": 1,
        "name": 'Andys Pizza',
        "logo": 'static/uploads/andys.png',
        "phone": '+(373) 797-111-11',
        "address": 'Ул. Мирча Чел Бэтрын 15',
        "website": 'www.andys.md'
    }
    promotion_info = {
        'background': "/uploads/None/no-img.jpg",
        'image': "static/uploads/sale.png",
        'title': "Скидка 10% на все виды коктелей",
        'description': "Разнообразный и богатый опыт укрепление и развитие структуры позволяет оценить значение новых предложений. Не следует, однако забывать, что новая модель организационной деятельности требуют от нас анализа новых предложений. Повседневная практика показывает, что начало повседневной работы по формированию позиции позволяет выполнять важные задания по разработке форм развития. Не следует, однако забывать, что новая модель организационной деятельности представляет собой интересный эксперимент проверки позиций, занимаемых участниками в отношении поставленных задач. Повседневная практика показывает, что рамки и место обучения кадров в значительной степени обуславливает создание новых предложений. Задача организации, в особенности же рамки и место обучения кадров в значительной степени обуславливает создание форм развития.",
        'help_text': "Хочешь принять участие? Заходи!",
        'post_text': "Я получил скидку 10% на коктейль. Рекомендую!",
        'allowed_providers': ['vk','fb','ok','ig','tw']
    }

    template_name = 'app/promotion.html'

    def get(self, request):
        form = self.form_class()
        if request.user and request.user.is_authenticated() and request.user.social_auth.filter(user_id=request.user.id):
            guest = Guest.objects.filter(user=request.user).first()
            if guest:
                form = self.form_class(initial={'email':guest.email, 'phone':guest.phone})
        else:
            logout(request)
        return render(request, self.template_name, {'promotion': self.promotion_info, 'company': self.company_info, 'form': form})

    def post(self, request):
        guest = Guest.objects.filter(user=request.user).first()
        company = get_object_or_404(Company, id=1)
        form = self.form_class(request.POST)
        form_error = 0
        if form.is_valid():
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            if not (phone or email):
                form_error = 1
            else:
                if guest:
                    guest = Guest(id=guest.id, user=request.user, phone=phone, email=email, company=company)
                else:
                    guest = Guest.create(request.user,phone,email,company)
                guest.save()
                vk_social = request.user.social_auth.filter(provider='vk-oauth2').first()
                if vk_social:
                    vk_token = vk_social.extra_data['access_token']
                    vk_api = VKApi(vk_social.uid,vk_token)
                    user_friends = vk_api.get_friends_list()
        return render(request, self.template_name, {'promotion': self.promotion_info, 'form': form, 'form_error': form_error, 'guest': guest, 'user_friends': user_friends, 'token': vk_token})