from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    discription = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    discription = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    discription = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100.00, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата обнавления')
    exist = models.BooleanField(default=True, verbose_name='существует')

    def __str__(self):
        return f'{self.name}'


class Order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    number_of_products_per_position = models.IntegerField(verbose_name='Кол-во товара')
    discount_per_item = models.IntegerField(verbose_name='Скидка')

    def __str__(self):
        return f'{self.number_of_products_per_position} - {self.product}'


class Order(models.Model):
    unique_number = models.IntegerField(verbose_name='уникальный номер')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    delivery_address = models.TextField(blank=True, verbose_name='адрес доставки')
    client_phone_number = models.TextField(blank=True, verbose_name='телефон клиента')
    Clients_full_name = models.TextField(blank=True, verbose_name='ФИО клиента')
    product = models.ManyToManyField(Product, through=Order_item)

    def __str__(self):
        return f'{self.Clients_full_name}'
