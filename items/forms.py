from .models import Items
from django.forms import ModelForm, TextInput, Textarea, NumberInput, ImageField

class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['title', 'cost', 'intro', 'text', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
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