from django.shortcuts import render
from .models import Client, Product, Sale

from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ClientForm
from .forms import ProductForm
from .forms import FamilyForm

def index(request):
    return render(request, 'mdpapp/index.html')

def dblists(request):
    return render(request, 'mdpapp/dblists.html')

def clients(request):
    """Lists Clients"""
    clients = Client.objects.order_by('client_name')
    context = {'clients': clients}
    return render(request, 'mdpapp/clients.html', context)

def products(request):
    """Lists Products"""
    products = Product.objects.order_by('product_name')
    context = {'products': products}
    return render(request, 'mdpapp/products.html', context)

def sales(request):
    """Lists Sales"""
    sales = Sale.objects.order_by('sale_date')
    context = {'sales': sales}
    return render(request, 'mdpapp/sales.html', context)

def sale(request, sale_id):
    """Show a single sale and all its movements."""
    sale = Sale.objects.get(id=sale_id)
    movements = sale.movement_set.order_by('id')
    context = {'sale': sales, 'movements': movements}
    return render(request, 'mdpapp/sale.html', context)

def create(request):
    return render(request, 'mdpapp/create.html')

def create_client(request):
    """Create a new client."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClientForm()
    else:
        # POST data submitted; process data. 
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('client_creation'))
    context = {'form': form}
    return render(request, 'mdpapp/new_client.html', context)

def create_family(request):
    """Create a new product family."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FamilyForm()
    else:
        # POST data submitted; process data. 
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('family_creation'))
    context = {'form': form}
    return render(request, 'mdpapp/new_family.html', context)

def create_product(request):
    """Create a new product."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ProductForm()
    else:
        # POST data submitted; process data. 
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product_creation'))
    context = {'form': form}
    return render(request, 'mdpapp/new_product.html', context)
