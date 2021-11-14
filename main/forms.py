from .models import Product
from django.forms import ModelForm, widgets, TextInput, Textarea



class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ["email", "playlist", "qty", "comment",]
        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите E-mail'
            }),
            "playlist": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на плейлист'
            }),
            "qty": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите коментарий'
            }),
            
        }
        