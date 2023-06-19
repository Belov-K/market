from django.db import models

class Product(models.Model):
    product_title=models.CharField('название товара', max_length=200)
    product_text=models.TextField('описание товара')
    pub_date=models.DateTimeField('дата публикации товара')

class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    author_name=models.CharField('автор отзыва', max_length=50)
    review_text=models.TextField('текст отзыва')
