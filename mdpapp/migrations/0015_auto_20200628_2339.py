# Generated by Django 3.0.6 on 2020-06-28 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdpapp', '0014_auto_20200624_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name']},
        ),
    ]
