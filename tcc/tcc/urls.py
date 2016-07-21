"""tcc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from polls.views import HomeRedirectView, HomeView

urlpatterns = [
    url(r'^$', HomeRedirectView.as_view()),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login, {'template_name': 'polls/login.html'}),
    url(r'^accounts/logout/$', logout_then_login, {'login_url': '/accounts/login/'}),
    url(r'^home$', login_required(HomeView.as_view(template_name='polls/index.html')), name='home'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)