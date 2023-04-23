from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from django.conf.urls import handler400, handler403, handler404, handler500
from.views import *
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addservice/', addservice, name='create'),
    path('contact/', contact, name='contact'),
    path('contact/', login, name='login'),
    path('service/int:<s_id>/', show_service, name='show_service')
]



handler400 = 'service.views.bad_request'
handler403 = 'service.views.permission_denied'
handler404 = 'service.views.page_not_found'
handler500 = 'service.views.server_error'