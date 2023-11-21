from django import forms
from myapp.models import Product, ImageModel

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'origin', 'color']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']
