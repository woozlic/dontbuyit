from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Form, CharField, ValidationError
from .models import Account
from django.contrib.auth.models import User

class UserRegistrationForm(ModelForm):

    password = CharField(widget=PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'id': 'formGroupPasswordInput',
            }))
    password_repeat = CharField(widget=PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль',
                'id': 'formGroupPasswordRepeatInput',
            }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

        widgets = {

            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш логин',
                'id': 'formGroupUsernameInput',
            }),

            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
                'id': 'formGroupFirstnameInput',
            }),

            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш адрес электронной почты',
                'id': 'formGroupEmailInput',

            }),
        }

    def clean_second_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_repeat']:
            raise ValidationError('Пароли не совпадают!')
        return cd['password_repeat']

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