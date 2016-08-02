from django.shortcuts import render, get_object_or_404
from app.models import Article
from api.vk import VKApi
from django.http import HttpResponseForbidden, HttpResponse

def home(request):
    message = 'test'
    vk_social = request.user.social_auth.get(provider='vk-oauth2')
    vk_token = vk_social.extra_data['access_token']
    vk_api = VKApi(vk_social.uid,vk_token)
    resp = vk_api.wall_post(message)
    return render(request, 'app/home.html', {'resp': resp})

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user_friends = []
    vk_token = 0
    if request.user and not request.user.is_anonymous():
    	vk_social = request.user.social_auth.get(provider='vk-oauth2')
    	vk_token = vk_social.extra_data['access_token']
    	vk_api = VKApi(vk_social.uid,vk_token)
    	user_friends = vk_api.get_friends_list()

    return render(request, 'app/item.html', {'article': article, 'user_friends': user_friends, 'token': vk_token})