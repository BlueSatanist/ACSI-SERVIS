# Generated by Django 4.2.7 on 2024-05-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_products_collist_products_color_products_dlay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='products',
            name='collist',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Количество листов'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цвет катриджа/тонера'),
        ),
        migrations.AlterField(
            model_name='products',
            name='connection',
            field=models.CharField(blank=True, null=True, verbose_name='Подключение'),
        ),
        migrations.AlterField(
            model_name='products',
            name='dlay',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Катридж/тонер редназначен для:'),
        ),
        migrations.AlterField(
            model_name='products',
            name='dopf',
            field=models.CharField(blank=True, null=True, verbose_name='Дополнительные функции (Для МФУ)'),
        ),
        migrations.AlterField(
            model_name='products',
            name='form',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Формат бумаги'),
        ),
        migrations.AlterField(
            model_name='products',
            name='interf',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Интерфейс сканера'),
        ),
        migrations.AlterField(
            model_name='products',
            name='model',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='products',
            name='plotn',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Плотность бумаги'),
        ),
        migrations.AlterField(
            model_name='products',
            name='pocr',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Покрытие бумаги'),
        ),
        migrations.AlterField(
            model_name='products',
            name='print_speed',
            field=models.CharField(blank=True, null=True, verbose_name='Разрешение для принтера или мфу/Разрядность для сканера'),
        ),
        migrations.AlterField(
            model_name='products',
            name='resolution',
            field=models.CharField(blank=True, null=True, verbose_name='Скорость печати'),
        ),
        migrations.AlterField(
            model_name='products',
            name='technology',
            field=models.CharField(blank=True, null=True, verbose_name='Технология'),
        ),
        migrations.AlterField(
            model_name='products',
            name='trays',
            field=models.CharField(blank=True, null=True, verbose_name='Лотки'),
        ),
        migrations.AlterField(
            model_name='products',
            name='typef',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Тип фасовки тонера'),
        ),
    ]