# Generated by Django 5.0.1 on 2024-02-14 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order'),
        ),
    ]
