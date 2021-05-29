from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('add/', views.add_item, name='add'),
    path('', views.show_page, name='all'),
    path('search/', views.post_search, name='post_search'),
    path('my_rents/', views.my_rents, name='my_rents'),
    path('my_rents/all', views.all_rents, name='all_rents'),
    path('<int:page_num>/', views.show_page, name='all_page'),
    path('<slug:category>/', views.show_page, name='category'),
    path('<slug:category>/<int:page_num>/', views.show_page, name='category_page'),
    path('<slug:category>/<slug:slug>_<int:pk>/', views.show_item_other, name='show_item_other'),
    path('<slug:category>/<slug:subcategory>/', views.show_page, name='subcategory'),
    path('<slug:category>/<slug:subcategory>/<int:page_num>/', views.show_page, name='subcategory_page'),
    path('<slug:category>/<slug:subcategory>/<slug:slug>_<int:pk>/', views.show_item, name='show_item'),
    path('<slug:category>/<slug:subcategory>/<slug:slug>_<int:pk>/edit', views.edit_item, name='edit_item'),
    path('ajax/load_subcategories', views.load_subcategories, name='ajax_load_subcategories'),
]
