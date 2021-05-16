from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Form, CharField, ValidationError, \
    Select, ImageField, FileInput
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

    nickname = CharField(max_length=50, widget=TextInput(attrs={'class': 'fadeIn second',
                                                                'placeholder': 'Ваш логин',
                                                                'name': 'login',
                                                                'id': 'login'}))
    password = CharField(max_length=50, widget=PasswordInput(attrs={'class': 'fadeIn third',
                                                                    'placeholder': 'Пароль',
                                                                    'name': 'login',
                                                                    'id': 'password'}))


class DashboardForm(Form):

    image = ImageField(widget=FileInput(attrs={
        'style': 'display: none;',
        'class': 'btn btn-dark',
        'id': 'file',
    }))
