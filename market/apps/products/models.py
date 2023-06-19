from django.db import models

class Product(models.Model):
    product_title=models.CharField('название товара', max_length=200)
    product_text=models.TextField('описание товара')
    pub_date=models.DateTimeField('дата публикации товара')
    price = models.IntegerField("цена товара", blank=True, null=True)
    rate = models.FloatField("рейтинг товара", blank=True, null=True)

    class Meta:
        verbose_name="Продукт"
        verbose_name_plural="Продукты"

class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    author_name=models.CharField('автор отзыва', max_length=50)
    review_text=models.TextField('текст отзыва')

    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзывы"