from django.shortcuts import render, get_object_or_404
from app.models import Company, Promotion, Visit, Guest, PromoCode
from api.vk import VKApi
from api.ok import Odnoklassniki, OdnoklassnikiError
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth import logout
from .forms import SaveUserData

def home(request):
    return render(request, 'app/home.html', {})

def get_promocode(request):
    if request.method == "POST":
        guest = Guest.objects.filter(pk=request.POST['guest']).first()
        if guest:
            promo_code = PromoCode.create(guest,request.POST['promo_code'])
            promo_code.save()
        return HttpResponse('ok')
    else:
        code = PromoCode.promo_gen()
        return HttpResponse(code)

def show_promotion(request):
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

    # нужно для создания гостя, без компании же нельзя
    company = get_object_or_404(Company, id=1)

    # Нужно определять переменные или есть другой выход?
    phone = None
    email = None
    guest = None
    user_photo = None
    form_error = 0

    if request.user and request.user.is_authenticated():
        guest = Guest.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = SaveUserData(request.POST)
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
    else:
        if guest:
            form = SaveUserData(initial={'email':guest.email, 'phone':guest.phone})
        else:
            form = SaveUserData()

    user_friends = []
    vk_token = 0
    if request.user and request.user.is_authenticated():
        vk_social = request.user.social_auth.filter(provider='vk-oauth2').first()
        if vk_social:
            vk_token = vk_social.extra_data['access_token']
            vk_api = VKApi(vk_social.uid,vk_token)
            user_friends = vk_api.get_friends_list()
            user_photo = vk_api.get_profile_data()[0]['photo_200']
        else:
            logout(request)

    args = {
        'promotion': promotion_info, 
        'company': company_info, 
        'user_friends': user_friends, 
        'token': vk_token,
        'user_photo': user_photo,
        'guest': guest,
        'form': form,
        'form_error': form_error
    }
    return render(request, 'app/promotion.html', args)