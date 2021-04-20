# Generated by Django 3.1.7 on 2021-04-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='prise',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
    ]
