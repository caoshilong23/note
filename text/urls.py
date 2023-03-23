from django.urls import path
from . import views

urlpatterns = [

    path('', views.text),
    path('up', views.up),
    path('delete', views.delete),
    path('change', views.change)
]