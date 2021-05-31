from django import forms
from .models import (Product, Purchase)
from home.models import User
from datetime import datetime
from django.core.exceptions import ValidationError


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'quantity': forms.NumberInput(attrs={
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


class UserAvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']


default_attrs = {
    'class': 'form-control'
}


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = [
            'is_active', 'is_staff', 'is_superuser', 'last_login',
            'created_at', 'updated_at', 'avatar', 'password'
        ]
        widgets = {
            'email': forms.EmailInput(attrs=default_attrs),
            'name': forms.TextInput(attrs=default_attrs),
            'phone': forms.TextInput(attrs=default_attrs),
            'address': forms.TextInput(attrs=default_attrs)
        }


class UserPasswordForm(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput(attrs=default_attrs))

    class Meta:
        model = User
        fields = ['password']

        widgets = {
            'password': forms.PasswordInput(attrs=default_attrs)
        }

    def clean(self):
        cleaned_data = super(UserPasswordForm, self).clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        if password != repassword:
            raise ValidationError("Passwords do not match")
        return cleaned_data
