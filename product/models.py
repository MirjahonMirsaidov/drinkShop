from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Brand(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    slug = models.SlugField()
    price = models.FloatField()
    size = models.CharField(max_length=255)
    stock_count = models.PositiveIntegerField()


