from django import forms
from .models import Client
from .models import Product
from .models import Family

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name','client_address','client_contact','client_email','client_note']

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['family_name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_family', 'product_note']