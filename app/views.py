from django.shortcuts import render, get_object_or_404, redirect
from app.models import Company, Promotion, Visit, Guest, PromoCode
from api.vk import VKApi
from django.conf import settings
from api.ok import Odnoklassniki, OdnoklassnikiError
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth import logout
from .forms import UserDataForm
from django.views.generic import View
import hashlib
import urllib.parse

class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html', {})

class PromotionView(View):

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
        logout(request)
        return render(request, self.template_name, {'promotion': self.promotion_info, 'company': self.company_info})

class PromotionAccessView(View):
    promotion_info = {
        'background': "/uploads/None/no-img.jpg",
        'image': "static/uploads/sale.png",
        'title': "Скидка 10% на все виды коктелей",
        'description': "Разнообразный и богатый опыт укрепление и развитие структуры позволяет оценить значение новых предложений. Не следует, однако забывать, что новая модель организационной деятельности требуют от нас анализа новых предложений. Повседневная практика показывает, что начало повседневной работы по формированию позиции позволяет выполнять важные задания по разработке форм развития. Не следует, однако забывать, что новая модель организационной деятельности представляет собой интересный эксперимент проверки позиций, занимаемых участниками в отношении поставленных задач. Повседневная практика показывает, что рамки и место обучения кадров в значительной степени обуславливает создание новых предложений. Задача организации, в особенности же рамки и место обучения кадров в значительной степени обуславливает создание форм развития.",
        'help_text': "Хочешь принять участие? Заходи!",
        'post_text': "Я получил скидку 10% на коктейль. Рекомендую!",
        'allowed_providers': ['vk','fb','ok','ig','tw']
    }
    form_class = UserDataForm
    template_name = 'app/promotion-access.html'
    def get(self, request):
        user_friends = {}
        token = None
        social = None
        pub_query = None
        form = self.form_class
        if request.user and request.user.is_authenticated() and request.user.social_auth.filter(user_id=request.user.id):
            guest = Guest.objects.filter(user=request.user).first()
            if guest:
                form = self.form_class(initial={'email':guest.email, 'phone':guest.phone})

            social = request.user.social_auth.filter(user_id=request.user.id).first()

            if social:
                token = social.extra_data['access_token']

                if social.provider == 'vk-oauth2':
                    vk_api = VKApi(social.uid,token)
                    user_friends = vk_api.get_friends_list()
                
                if social.provider == 'odnoklassniki-oauth2':
                    app_id = settings.SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_KEY
                    s_key = settings.SOCIAL_AUTH_ODNOKLASSNIKI_OAUTH2_SECRET
                    
                    attachment_raw = '{"media": [{"type": "text", "text": "' + self.promotion_info['post_text'] + '"}]}'
                    attachment = urllib.parse.quote(attachment_raw.encode("utf-8"))

                    signature_raw = 'st.attachment=' + attachment_raw + s_key
                    signature = hashlib.md5(signature_raw.encode('utf-8')).hexdigest()
                    
                    pub_query = 'https://connect.ok.ru/dk?st.cmd=WidgetMediatopicPost&st.app=' + app_id
                    pub_query += '&st.attachment=' + attachment
                    pub_query += '&st.signature=' + signature
                    pub_query += '&st.popup=on&st.silent=off';
                    pub_query += '&st.access_token=' + token;
                    pub_query += '-----' + signature_raw

            return render(request, self.template_name, {'promotion': self.promotion_info, 'form': form, 'guest': guest, 'user_friends': user_friends, 'token': token, 'provider': social.provider, 'pub_query': pub_query})
        else:
            return redirect('/')

    def post(self, request):
        guest = Guest.objects.filter(pk=request.POST['guest']).first()
        company = get_object_or_404(Company, id=1)
        if guest:
            guest = Guest(id=guest.id, user=request.user, phone=request.POST['phone'], email=request.POST['email'], company=company)
        else:
            guest = Guest.create(request.user,request.POST['phone'],request.POST['email'],company)
        guest.save()    
        promo_code = PromoCode.create(guest,request.POST['promo_code'])
        promo_code.save()

        return HttpResponse('done');       