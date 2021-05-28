from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'single-select w-100 mb-3 form-control'
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }