from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import PromotionView, PromotionAccessView

urlpatterns = patterns('',
	url(r'', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^promotion/(?P<promotion_id>[0-9]+)/$', 'app.views.show_promotion', name='promotion'),
    url(r'^$', PromotionView.as_view()),
    url(r'^access/$', PromotionAccessView.as_view())
)