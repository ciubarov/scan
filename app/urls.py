from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^item/(?P<article_id>[0-9]+)/$', 'app.views.show_article', name='article'),
    url('', include('django.contrib.auth.urls', namespace='auth')) 
)
