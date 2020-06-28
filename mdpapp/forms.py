from django import forms
from .models import Client
from .models import Product
from .models import Family
from .models import Movement
from .models import Sale

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

class SaleForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.order_by('client_name'), label="Cliente")
    class Meta:
        model = Sale
        fields = ['client', 'sale_note']

class MovementForm(forms.ModelForm):
    class Meta:
        model = Movement
        fields = ['movement_product', 'movement_quantity','movement_purchase_price', 'movement_selling_price']