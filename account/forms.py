from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Form, CharField, ValidationError, \
    Select, ImageField, FileInput, BooleanField, CheckboxInput
from django.contrib.auth.models import User
from .models import Profile
import re


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
    
    agreement = BooleanField(required=True, help_text='Я согласен с пользовательским соглашением',
                             widget=CheckboxInput(attrs={
                                'class': 'form-check-input',
                                'id': 'agreement'
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

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')

        if len(first_name) < 2 or len(first_name) > 20:
            raise ValidationError('Имя должно содержать от 2 до 20 символов')
        if re.fullmatch(r'[A-Za-zА-Яа-я]{2,}', first_name):
            pass
        else:
            raise ValidationError('Имя должно содержать только буквы русского или английского алфавита')

        if re.fullmatch(r'[A-Za-z0-9@_#$%\-^&+=]{6,}', username):
            pass
        else:
            raise ValidationError('Логин должен состоять из латинских букв, цифр и символов @_#$%-^&+= и иметь длину '
                                  'минимум 6 символов')

        if len(password) < 6 or len(password) > 18:
            raise ValidationError('Пароль должен иметь длину от 6 до 18 символов')

        if password != password_repeat:
            raise ValidationError('Пароли не совпадают!')

        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{6,}', password):
            pass
        else:
            raise ValidationError('Пароль должен состоять из латинских букв, цифр и символов @#$%^&+= и иметь длину '
                                  'не меньше 6 и не больше 18 символов')


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
        fields = ('gender', 'phone_number')
        genders = [('мужской', 'мужской'), ('мужской', 'мужской')]

        widgets = {
            'gender': Select(choices=genders, attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['gender'].required = True

    def clean_phone_number(self):
        cd = self.cleaned_data
        phone_number = cd['phone_number']
        try:
            int(phone_number)
        except ValueError:
            raise ValidationError('Телефон должен состоять из 10 цифр и начинаться с цифры 9')
        if len(phone_number) != 10:
            raise ValidationError('Телефон должен состоять из 10 цифр')
        if str(phone_number)[0] != '9':
            raise ValidationError('Телефон должен начинаться с 9')
        if User.objects.filter(profile__phone_number=str(phone_number)).exists():
            raise ValidationError('Такой номер телефона уже зарегистрирован')
        return phone_number


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
        'id': 'file'
    }))
