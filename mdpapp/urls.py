"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Query Menu
    path('dblists/', views.dblists, name='dblists'),
    # List Clients
    path('dblists/clients/', views.clients, name='clients'),
    # List Products
    path('dblists/products/', views.products, name='products'),
    # List Sales
    path('dblists/sales/', views.sales, name='sales'),
    # List Movements in a Sale
    path('dblists/sales/<int:sale_id>/', views.sale, name='sale'),
]