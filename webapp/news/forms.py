from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "image": ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'  # разрешаем только изображения
            })
            


        }
