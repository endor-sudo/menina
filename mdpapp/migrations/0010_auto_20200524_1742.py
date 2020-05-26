# Generated by Django 3.0.6 on 2020-05-24 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdpapp', '0009_auto_20200524_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdpapp.Sale', verbose_name='Venda'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da Venda'),
        ),
    ]
