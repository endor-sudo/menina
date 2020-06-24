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
    # All sales of today
    path('dblists/td_sales/<int:dia>/<int:page>/', views.todays_sales, name='td_sales'),
    # Sales of the month by day
    path('dblists/mn_sales/<int:month>', views.months_sales, name='mn_sales'),
    # Sales of the year by month
    path('dblists/yr_sales/', views.years_sales, name='yr_sales'),
    # List Movements in a Sale
    path('dblists/sales/<int:sale_id>/', views.sale, name='sale'),
    # Choose what to create
    path('lancar/', views.create, name='creation'),
    # Create Client
    path('lancar/client/', views.create_client, name='client_creation'),
    # Create Family
    path('lancar/family/', views.create_family, name='family_creation'),
    # Create Product
    path('lancar/product/', views.create_product, name='product_creation'),
    # Create Sale
    path('lancar/sale/', views.create_sale, name='sale_creation'),
]