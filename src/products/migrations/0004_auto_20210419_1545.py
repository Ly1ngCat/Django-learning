# Generated by Django 3.1.7 on 2021-04-19 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prise',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
