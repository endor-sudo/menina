# Generated by Django 3.0.6 on 2020-06-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdpapp', '0013_auto_20200602_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_total',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
