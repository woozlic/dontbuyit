from .models import Items
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ImageField, FileInput, Form, Select

class ItemsForm(ModelForm):
    class Meta:
        categories = [('electronic', 'Электроника'), ('instruments', 'Инструменты'),
                      ('transport', 'Средства передвижения'), ('wear', 'Одежда, обувь'),
                      ('kids', 'Детские товары'), ('other', 'Прочее')]
        model = Items
        fields = ['title', 'cost', 'category', 'intro', 'text', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            'category': Select(choices=categories, attrs={
                'class': 'form-control'
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание товара'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полное описание товара'
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость в рублях'
            })
        }
