# Generated by Django 3.0.6 on 2020-05-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdpapp', '0010_auto_20200524_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_note',
            field=models.CharField(max_length=200, null=True, verbose_name='Observações'),
        ),
    ]
