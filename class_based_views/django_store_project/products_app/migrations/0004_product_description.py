# Generated by Django 5.0.2 on 2024-04-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_alter_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
