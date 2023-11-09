from django import forms
from myapp.models import Product

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'origin', 'color']

class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")
