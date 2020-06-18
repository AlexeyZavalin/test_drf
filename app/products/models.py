from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Наименование категории')
    image = models.ImageField(max_length=100, upload_to='categories')
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return self.title


class Kitchen(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    PAYMENT_TYPES = [('OL', 'Оплата онлайн'),
                     ('CS', 'Оплата наличными, при получении'),
                     ('CA', 'Оплата картой, при получении')]
    payment_type = models.CharField(max_length=2, choices=PAYMENT_TYPES, unique=True)

    def __str__(self):
        return self.payment_type


class Menu(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Наименование категории в меню заведения')

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=128,
                            verbose_name='Наименование заведения')
    slug = models.SlugField(max_length=50, default='')
    category = models.ManyToManyField(Category, verbose_name='Категории')
    kitchens = models.ManyToManyField(Kitchen, verbose_name='Кухни')
    logo = models.ImageField(max_length=100,
                             upload_to='logos',
                             verbose_name='Логотип заведения')
    image = models.ImageField(max_length=100,
                              upload_to='establishments',
                              verbose_name='Фото заведения')
    popular = models.BooleanField(default=False, verbose_name='Популярное заведение')
    payment = models.ManyToManyField(PaymentType, verbose_name='Способы оплаты')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Наименование товара')
    price = models.DecimalField(decimal_places=2,
                                max_digits=9,
                                verbose_name='Цена товара')
    image = models.ImageField(max_length=100, upload_to='products', verbose_name='Фото товара',
                              default='products/default.png')
    establishment = models.ForeignKey(Establishment,
                                      on_delete=models.CASCADE,
                                      verbose_name='Заведение')
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)
    ingredients = models.TextField(max_length=256,
                                   null=True,
                                   blank=True,
                                   verbose_name='Ингредиенты')
    popular = models.BooleanField(default=False,
                                  verbose_name='Популярный товар')
    promo = models.BooleanField(default=False, verbose_name='Акционный товар')

    def __str__(self):
        return self.title


class Review(models.Model):
    reviewer_name = models.CharField(max_length=40)
    review_text = models.TextField()
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE,
                                      related_name='reviews')
    phone = models.CharField(max_length=18)
    rating = models.SmallIntegerField()
