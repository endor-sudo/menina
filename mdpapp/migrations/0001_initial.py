# Generated by Django 3.0.6 on 2020-05-24 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200, unique=True, verbose_name='Nome')),
                ('client_address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('client_contact', models.CharField(max_length=200, verbose_name='Contacto')),
                ('client_email', models.EmailField(max_length=200, null=True, verbose_name='Email')),
                ('client_notes', models.CharField(max_length=200, verbose_name='Observações')),
                ('client_date_added', models.DateTimeField(auto_now_add=True, verbose_name='Data Adicionado')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=200, unique=True, verbose_name='Família')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True, verbose_name='Data Adicionado')),
                ('sale_note', models.CharField(max_length=200, verbose_name='Observações')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mdpapp.Clients', verbose_name='Clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True, verbose_name='Nome')),
                ('product_notes', models.CharField(max_length=200, verbose_name='Observações')),
                ('product_date_added', models.DateTimeField(auto_now_add=True, verbose_name='Data Adicionado')),
                ('product_family', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mdpapp.Family', verbose_name='Família')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movement_quantity', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Quantidade')),
                ('movement_purchase_price', models.DecimalField(decimal_places=3, help_text="Introduza '0' para ignorar.", max_digits=7, null=True, verbose_name='Preço de Custo')),
                ('movement_selling_price', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Preço de Venda')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mdpapp.Products', verbose_name='Produto')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mdpapp.Sales', verbose_name='Venda')),
            ],
        ),
    ]
