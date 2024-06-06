from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Модель')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    brand = models.CharField(max_length=150, blank=True, null=True, verbose_name='Бренд')
    model = models.CharField(max_length=150, blank=True, null=True, verbose_name='Модель')
    technology = models.CharField(blank=True, null=True, verbose_name='Технология')
    resolution = models.CharField(blank=True, null=True, verbose_name='Скорость печати')
    print_speed = models.CharField(blank=True, null=True, verbose_name='Разрешение для принтера или мфу/Разрядность для сканера')
    trays = models.CharField(blank=True, null=True, verbose_name='Лотки')
    connection = models.CharField(blank=True, null=True, verbose_name='Подключение/Интерфейс сканера')
    dopf = models.CharField(blank=True, null=True, verbose_name='Дополнительные функции (Для МФУ)')
    dlay = models.CharField(max_length=150, blank=True, null=True, verbose_name='Катридж/тонер редназначен для:')
    typef = models.CharField(max_length=150, blank=True, null=True, verbose_name='Тип фасовки тонера')
    resurs = models.CharField(max_length=150, blank=True, null=True, verbose_name='Ресурс картриджа')
    color = models.CharField(max_length=150, blank=True, null=True, verbose_name='Цвет катриджа/тонера')
    form = models.CharField(max_length=150, blank=True, null=True, verbose_name='Формат бумаги')
    pocr = models.CharField(max_length=150, blank=True, null=True, verbose_name='Покрытие бумаги')
    plotn = models.CharField(max_length=150, blank=True, null=True, verbose_name='Плотность бумаги')
    collist = models.CharField(max_length=150, blank=True, null=True, verbose_name='Количество листов')
    





    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    

    def display_id(self):
        return f"{self.id:05}"


    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price
    

    