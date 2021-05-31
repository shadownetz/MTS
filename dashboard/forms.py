from django import forms
from .models import (Product, Purchase)
from datetime import datetime


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


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ['created_at', 'quantity', 'product']
        widgets = {
            # 'product': forms.Select(attrs={
            #     'class': 'single-select w-100 mb-3 form-control'
            # }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            # 'quantity': forms.NumberInput(attrs={
            #     'class': 'form-control'
            # })
        }

    def save(self, commit=True):
        instance = super(PurchaseForm, self).save(commit=False)
        instance.updated_at = datetime.now()
        if commit:
            instance.save()
        return instance
