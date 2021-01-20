from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view
    (success_url=reverse_lazy('account:password_change_done')), name='password_change'),

    path('register/', views.auth_register, name='register'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.dashboard, name="dashboard")
    # path('login/', views.auth_login, name='login'),
]
