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

def show_promotion(request, promotion_id):
    # logout(request)
    promotion = get_object_or_404(Promotion, id=promotion_id)
    company = get_object_or_404(Company, id=promotion.company_id)
    user_friends = []
    vk_token = 0
    promo_code = id_generator()
    if request.user and not request.user.is_anonymous():
        vk_social = request.user.social_auth.get(provider='vk-oauth2')
        vk_token = vk_social.extra_data['access_token']
        vk_api = VKApi(vk_social.uid,vk_token)
        user_friends = vk_api.get_friends_list()
    return render(request, 'app/promotion.html', {'promotion': promotion, 'company': company, 'user_friends': user_friends, 'token': vk_token, 'promo_code': promo_code})