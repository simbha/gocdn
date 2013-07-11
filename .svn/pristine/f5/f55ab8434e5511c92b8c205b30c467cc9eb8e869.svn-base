# encoding: utf-8
__author__ = 'yasemenkarakoc'

from django import forms
from gocdn.product.models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']
