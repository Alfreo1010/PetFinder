# Generated by Django 5.0.1 on 2024-02-14 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_shippingaddress_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
