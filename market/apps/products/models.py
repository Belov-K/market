from django.db import models

class Product(models.Model):
    product_title=models.CharField('название продукта', max_length=200)
    product_text=models.TextField('описание продукта')
    pub_date=models.DateTimeField('дата публикации продукта')

class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    author_name=models.CharField('автор отзыва', max_length=50)
    review_text=models.TextField('текст отзыва')
