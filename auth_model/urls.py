from django.conf.urls import url
from . import views

app_name = 'auth_model'

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^auth_view/$', views.auth_view, name='auth_view'),
    url(r'^success/$', views.success, name='success'),
    url(r'^logout/$', views.logout, name='logout'),
]
