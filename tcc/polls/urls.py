from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListaMedalhasView.as_view(), name='index'),
    url(r'^$', views.AvatarUsuario.as_view(), name='index'),
]