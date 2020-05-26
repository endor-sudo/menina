from django.shortcuts import render
from .models import Client, Product, Sale

def index(request):
    return render(request, 'mdpapp/index.html')

def dblists(request):
    return render(request, 'mdpapp/dblists.html')

def clients(request):
    """Listar Clientes"""
    clients = Client.objects.order_by('client_name')
    context = {'clients': clients}
    return render(request, 'mdpapp/clients.html', context)

def products(request):
    """Listar Produtos"""
    products = Product.objects.order_by('product_name')
    context = {'products': products}
    return render(request, 'mdpapp/products.html', context)

def sales(request):
    """Listar Produtos"""
    sales = Sale.objects.order_by('sale_date')
    context = {'sales': sales}
    return render(request, 'mdpapp/sales.html', context)
