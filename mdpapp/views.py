from django.shortcuts import render
from .models import Client, Product, Sale

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
