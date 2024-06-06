# Generated by Django 4.2.7 on 2024-05-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_products_description1_products_description3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description4',
        ),
        migrations.RemoveField(
            model_name='products',
            name='description5',
        ),
        migrations.AddField(
            model_name='products',
            name='brand',
            field=models.TextField(blank=True, null=True, verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='products',
            name='connection',
            field=models.TextField(blank=True, null=True, verbose_name='Подключение'),
        ),
        migrations.AddField(
            model_name='products',
            name='print_speed',
            field=models.TextField(blank=True, null=True, verbose_name='Разрешение'),
        ),
        migrations.AddField(
            model_name='products',
            name='resolution',
            field=models.TextField(blank=True, null=True, verbose_name='Скорость печати'),
        ),
        migrations.AddField(
            model_name='products',
            name='technology',
            field=models.TextField(blank=True, null=True, verbose_name='Технология'),
        ),
        migrations.AddField(
            model_name='products',
            name='trays',
            field=models.TextField(blank=True, null=True, verbose_name='Лотки'),
        ),
    ]