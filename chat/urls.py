from django.urls import path

from . import views

urlpatterns = [
    path('', views.room, name='chat_index'),
    path('<str:first>_<str:second>/', views.room, name='room'),
]