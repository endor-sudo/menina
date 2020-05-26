from django.shortcuts import render
from .models import Client

def index(request):
    return render(request, 'mdpapp/index.html')

def clients(request):
    """Listar Clientes"""
    clients = Client.objects.order_by('client_name')
    context = {'clients': clients}
    return render(request, 'mdpapp/clients.html', context)