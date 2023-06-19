import datetime
from django.db import models

from django.utils import timezone

class Product(models.Model):
    """
    Текст продукт
    """
    product_title=models.CharField('название товара', max_length=200)
    product_text=models.TextField('описание товара')
    pub_date=models.DateTimeField('дата публикации товара', blank=True, null=True)
    price = models.IntegerField("цена товара", blank=True, null=True)
    rate = models.FloatField("рейтинг товара", blank=True, null=True)

    class Meta:
        verbose_name="Продукт"
        verbose_name_plural="Продукты"

    def __str__(self):
        return f"{self.id}# Продукт - {self.product_title}"

class Review(models.Model):
    """
    Текст отзыв
    """
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    author_name=models.CharField('автор отзыва', max_length=50)
    review_text=models.TextField('текст отзыва')

    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзывы"

    def __str__(self):
        return f"{self.id}# Отзыв - {self.author_name}"

class ProductImage(models.Model):
    """
    Изображение продукта
    """
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField('изображение')

    class Meta:
        verbose_name="Изображение продукта"
        verbose_name_plural="Изображения продуктов"

    def __str__(self):
        return f"{self.id}# Изображение"