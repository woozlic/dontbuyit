from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Form, CharField
from .models import Account

class LoginForm(Form):
    # email = CharField(max_length=50, widget=EmailInput(attrs={'class': 'form-control',
    #                                                           'placeholder': 'Адрес электронной почты'}))
    nickname = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Введите ваш логин'}))
    password = CharField(max_length=50, widget=PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Пароль'}))
    # следующее для ModelForm
    # class Meta:
    #     fields = ['mail', 'login', 'password']
    #     widgets = {
    #         'mail': EmailInput(attrs={
    #             'class': 'form-control',
    #         }),
    #         'login': TextInput(attrs={
    #             'class': 'form-control',
    #         }),
    #         'password': PasswordInput(attrs={
    #             'class': 'form-control',
    #         }),
    #     }