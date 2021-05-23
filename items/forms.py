from .models import Items, SubCategories
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ImageField, FileInput, Form, Select, \
    ValidationError, ModelChoiceField
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


class PeriodChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f""


class ItemsForm(ModelForm):

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
            'subcategory': Select(attrs={
                'class': 'form-control',
                'id': 'subcategory',
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
                'placeholder': 'Полное описание товара'
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control',
                'id': 'cost',
                'placeholder': 'Стоимость в рублях'
            }),
            'deposit': NumberInput(attrs={
                'class': 'form-control',
                'id': 'deposit',
                'placeholder': 'Залог в рублях'
            }),
            'full_price': NumberInput(attrs={
                'class': 'form-control',
                'id': 'full_price',
                'placeholder': 'Цена новой вещи в рублях'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = SubCategories.objects.none()
        self.fields['category'].required = True
        if 'category' in self.data:
            try:
                category = int(self.data.get('category'))
                self.fields['subcategory'].queryset = SubCategories.objects.filter(category__id=category).order_by('subcategory_name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('subcategory_name')

    def clean_subcategory(self):
        cd = self.cleaned_data
        if cd['subcategory'] is None and cd['category'].category_name != 'Разное':
            raise ValidationError('Пожалуйста, выберите Подкатегорию из списка')

        return cd['subcategory']

    def clean_image_1(self):
        img_extensions = ('.jpg', '.jpeg', '.png')
        cd = self.cleaned_data
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
