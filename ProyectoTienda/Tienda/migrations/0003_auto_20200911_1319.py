# Generated by Django 3.0.8 on 2020-09-11 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_auto_20200909_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='prod_pedido',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]