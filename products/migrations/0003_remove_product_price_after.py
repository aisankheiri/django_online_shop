# Generated by Django 4.0.2 on 2023-03-16 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price_after'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_after',
        ),
    ]