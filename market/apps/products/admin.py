from django.contrib import admin

from .models import Product, Review, ProductImage

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ProductImage)