from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all, name='all'),
    path('add/', views.add_item, name='add'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item_detail')
]
