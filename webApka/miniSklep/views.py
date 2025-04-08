from django.shortcuts import render
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        labels = {
            'name': 'Nazwa produktu',
            'price': 'Cena (PLN)'
        }