from django.urls import path

from . import views

urlpatterns = [

    path('login', views.login),
    path('logon', views.logon),
    path('logout', views.logout)

]
