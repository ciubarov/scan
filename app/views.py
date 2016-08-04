from django.shortcuts import render, get_object_or_404
from app.models import Company, Promotion
from api.vk import VKApi
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth import logout
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def home(request):
    return render(request, 'app/home.html', {})

def show_promotion(request):
# def show_promotion(request, promotion_id):
    # logout(request)
    # promotion = get_object_or_404(Promotion, id=promotion_id)
    # company = get_object_or_404(Company, id=promotion.company_id)
    company_info = {
        "name": 'Andys Pizza',
        "logo": 'static/uploads/andys.png',
        "phone": '+(373) 797-111-11',
        "address": 'Ул. Мирча Чел Бэтрын 15',
        "website": 'www.andys.md'
    }
    promotion_info = {
        'background': "/uploads/None/no-img.jpg",
        'image': "/uploads/None/no-img.jpg",
        'title': "Скидка 10% на все виды коктелей",
        'description': "Разнообразный и богатый опыт укрепление и развитие структуры позволяет оценить значение новых предложений. Не следует, однако забывать, что новая модель организационной деятельности требуют от нас анализа новых предложений. Повседневная практика показывает, что начало повседневной работы по формированию позиции позволяет выполнять важные задания по разработке форм развития. Не следует, однако забывать, что новая модель организационной деятельности представляет собой интересный эксперимент проверки позиций, занимаемых участниками в отношении поставленных задач. Повседневная практика показывает, что рамки и место обучения кадров в значительной степени обуславливает создание новых предложений. Задача организации, в особенности же рамки и место обучения кадров в значительной степени обуславливает создание форм развития.",
        'help_text': "Хочешь принять участие? Заходи!",
        'post_text': "Я получил скидку 10% на коктейль. Рекомендую!",
        'allowed_providers': ['vk','fb','ok','ig','tw']
    }
    user_friends = []
    vk_token = 0
    promo_code = id_generator()
    if request.user and not request.user.is_anonymous():
        vk_social = request.user.social_auth.get(provider='vk-oauth2')
        vk_token = vk_social.extra_data['access_token']
        vk_api = VKApi(vk_social.uid,vk_token)
        user_friends = vk_api.get_friends_list()
    return render(request, 'app/promotion.html', {'promotion': promotion_info, 'company': company_info, 'user_friends': user_friends, 'token': vk_token, 'promo_code': promo_code})