# Generated by Django 3.0.6 on 2020-05-24 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdpapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
    ]
