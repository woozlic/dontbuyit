from .models import Items
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ImageField, FileInput, Form, Select, \
    ValidationError, ModelChoiceField

import os


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
        fields = ['title', 'cost', 'category', 'text', 'image_1', 'image_2', 'image_3', 'deposit', 'full_price', 'period']

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
            'image': FileInput(attrs={
                'style': 'display: none;',
                'id': 'image',
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
            })
        }

    def clean_image(self):
        img_extensions = ('.jpg', '.jpeg', '.png')
        cd = self.cleaned_data
        ext = os.path.splitext(cd['image'].name)[1]
        if ext not in img_extensions:
            raise ValidationError('Изображение должно быть формата .jpg, .jpeg, или .png')
        return cd['image']