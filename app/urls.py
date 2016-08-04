from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^promotion/(?P<promotion_id>[0-9]+)/$', 'app.views.show_promotion', name='promotion'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^tinymce/', include('tinymce.urls'))
)
