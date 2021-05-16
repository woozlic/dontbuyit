from django.urls import path, include
from . import views

app_name = 'items'

urlpatterns = [
    path('add/', views.add_item, name='add'),

    path('', views.show_page, name='all'),
    path('<int:page_num>/', views.show_page, name='all_page'),
    path('<slug:category>/', views.show_page, name='category'),
    path('<slug:category>/<int:page_num>/', views.show_page, name='category_page'),
    path('<slug:category>/<slug:slug>_<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),


]
