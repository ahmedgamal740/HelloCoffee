# Generated by Django 3.2.5 on 2021-08-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
        ('accounts', '0003_alter_userprofile_product_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
