from django import forms
from myapp.models import Product

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']