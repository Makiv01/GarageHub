# Generated by Django 5.0.1 on 2024-03-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_manufacturer_alter_product_manufacturer_model_car_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year_from',
            field=models.IntegerField(default=2024),
        ),
        migrations.AddField(
            model_name='product',
            name='year_to',
            field=models.IntegerField(default=2024),
        ),
    ]
