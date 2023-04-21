from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('dlogin',views.dlogin,name='dlogin'),
    path('login',views.login,name='login'),
    path('plogin',views.plogin,name='plogin'),
    path('logout',views.logout,name='logout'),
]