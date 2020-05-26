from django.contrib import admin
from mdpapp.models import Client, Family, Product, Sale, Movement

admin.site.register(Client)
admin.site.register(Family)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Movement)