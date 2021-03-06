from .models import Items, SubCategories, Categories
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ImageField, FileInput, Form, Select, \
    ValidationError, ModelChoiceField, CharField
from django import forms

import os


class SearchForm(forms.Form):
    query = forms.CharField(widget=TextInput(attrs={
        'class': 'form-control mr-sm-2',
        'placeholder': 'Поиск',
        'type': 'search',
    }))


class SubCategoryChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.category.category_name}: {obj.subcategory_name}"


class ForgetfulSelect(Select):
    """
    Custom widget for Select that doesn't remember old values
    """
    def get_context(self, name, value, attrs):
        # value = None
        return super().get_context(name, value, attrs)


class PeriodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f""


class ItemsForm(ModelForm):
    subcategory = CharField(widget=Select(attrs={
        'class': 'form-control',
        'id': 'subcategory',
    }))

    class Meta:
        categories = [('electronic', 'Электроника'), ('instruments', 'Инструменты'), ('house', 'Для дома'),
                      ('transport', 'Средства передвижения'), ('wear', 'Одежда, обувь'),
                      ('furniture', 'Мебель'), ('kids', 'Детские товары'), ('other', 'Прочее')]

        periods = [('1 час', '1 час'), ('1 сутки', '1 сутки'), ('3 суток', '3 суток'), ('7 суток', '7 суток'),
                   ('1 месяц', '1 месяц')]

        model = Items

        fields = ['title', 'cost', 'category', 'subcategory', 'text', 'image_1', 'image_2', 'image_3', 'deposit', 'full_price', 'period']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'id': 'title',
                'placeholder': 'Название товара'
            }),
            'category': Select(choices=categories, attrs={
                'class': 'form-control',
                'id': 'category',
            }),
            'period': Select(choices=periods, attrs={
                'class': 'form-control',
                'id': 'period',
            }),
            'image_1': FileInput(attrs={
                # 'style': 'display: none;',
                'class': 'image-upload',
                'id': 'image-1',
                'onchange': 'changeImage(event, "img1")'
            }),
            'image_2': FileInput(attrs={
                'class': 'image-upload',
                'id': 'image-2',
                'onchange': 'changeImage(event, "img2")',
            }),
            'image_3': FileInput(attrs={
                'class': 'image-upload',
                'id': 'image-3',
                'onchange': 'changeImage(event, "img3")',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'id': 'text',
                'placeholder': 'Полное описание товара',
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control',
                'id': 'cost',
                'placeholder': 'Стоимость в рублях',
                'value': '1000'
            }),
            'deposit': NumberInput(attrs={
                'class': 'form-control',
                'id': 'deposit',
                'placeholder': 'Залог в рублях',
                'value': '5000'
            }),
            'full_price': NumberInput(attrs={
                'class': 'form-control',
                'id': 'full_price',
                'placeholder': 'Цена новой вещи в рублях',
                'value': '10000'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ItemsForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = SubCategories.objects.none()
        self.fields['category'].required = True
        self.fields['subcategory'].required = False
        self.fields['image_1'].required = False
        self.fields['text'].initial = 'Это объявление не является настоящим и было создано для тестирования сервиса. Спасибо за понимание'  # added for test
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                subs = SubCategories.objects.filter(category_id=category_id).order_by('subcategory_name')
                self.fields['subcategory'].queryset = subs
            except(ValueError, TypeError) as err:
                print(err)
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('subcategory_name')

    def clean_title(self):
        cd = self.cleaned_data
        if len(str(cd['title'])) > 50:
            raise ValidationError('Заголовок должен быть менее 50 символов')
        if len(str(cd['title'])) < 8:
            raise ValidationError('Заголовок должен быть больше 8 символов')
        return cd['title']

    def clean_cost(self):
        cd = self.cleaned_data
        try:
            float(cd['cost'])
        except ValueError:
            raise ValidationError('Цена должна быть числом')
        if int(cd['cost']) > 100000000:
            raise ValidationError('Кажется, это слишком большая цена')
        if int(cd['cost']) < 0:
            raise ValidationError('Пожалуйста, укажите цену не меньше нуля')
        return cd['cost']

    def clean_deposit(self):
        cd = self.cleaned_data
        try:
            float(cd['deposit'])
        except ValueError:
            raise ValidationError('Цена должна быть числом')
        if int(cd['deposit']) > 100000000:
            raise ValidationError('Кажется, это слишком большая цена')
        if int(cd['deposit']) < 0:
            raise ValidationError('Пожалуйста, укажите цену не меньше нуля')
        return cd['deposit']

    def clean_full_price(self):
        cd = self.cleaned_data
        try:
            float(cd['full_price'])
        except ValueError:
            raise ValidationError('Цена должна быть числом')
        if int(cd['full_price']) > 100000000:
            raise ValidationError('Кажется, это слишком большая цена')
        if int(cd['full_price']) < 0:
            raise ValidationError('Пожалуйста, укажите цену не меньше нуля')
        return cd['full_price']

    def clean_subcategory(self):
        cd = self.cleaned_data

        try:
            if 'category' in cd:
                subcategory = SubCategories.objects.filter(category__category_name=cd['category']).get(subcategory_name=cd['subcategory'])
            else:
                raise ValidationError('Пожалуйста, выберите Подкатегорию из списка')
        except SubCategories.DoesNotExist:
            subcategory = None
        if 'category' in cd and subcategory is None and cd['category'].category_name != 'Разное':
            raise ValidationError('Пожалуйста, выберите Подкатегорию из списка')

        return subcategory

    def clean_image_1(self):
        img_extensions = ('.jpg', '.jpeg', '.png')
        cd = self.cleaned_data
        if not cd['image_1']:
            raise ValidationError('Загрузите как минимум одно изображение')
        ext = os.path.splitext(cd['image_1'].name)[1]
        if ext not in img_extensions:
            raise ValidationError('Изображение должно быть формата .jpg, .jpeg, или .png')
        return cd['image_1']

    def clean_image_2(self):
        img_extensions = ('.jpg', '.jpeg', '.png')
        cd = self.cleaned_data
        if cd['image_2']:
            ext = os.path.splitext(cd['image_2'].name)[1]
            if ext not in img_extensions:
                raise ValidationError('Изображение должно быть формата .jpg, .jpeg, или .png')
        return cd['image_2']

    def clean_image_3(self):
        img_extensions = ('.jpg', '.jpeg', '.png')
        cd = self.cleaned_data
        if cd['image_3']:
            ext = os.path.splitext(cd['image_3'].name)[1]
            if ext not in img_extensions:
                raise ValidationError('Изображение должно быть формата .jpg, .jpeg, или .png')
        return cd['image_3']
