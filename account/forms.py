from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Form, CharField, ValidationError, Select
from django.contrib.auth.models import User
from .models import Profile

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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
            }),

            'email': EmailInput(attrs={
                'class': 'form-control',
            }),
        }

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('gender',)
        genders = [('мужской', 'мужской'), ('женский', 'женский')]

        widgets = {
            'gender': Select(choices=genders, attrs={'class': 'form-control'})
        }
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