# Generated by Django 5.0.2 on 2024-04-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0004_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
