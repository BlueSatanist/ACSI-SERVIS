# Generated by Django 4.2.7 on 2024-05-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_alter_products_brand_alter_products_collist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Изображение'),
        ),
    ]
