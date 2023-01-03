from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('mypage/',views.mypage)
]