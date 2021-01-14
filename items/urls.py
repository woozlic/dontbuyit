from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_page, name='all'),
    path('add/', views.add_item, name='add'),
    path('<str:category>/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('<int:page_num>/', views.show_page, name='show_page')
]
