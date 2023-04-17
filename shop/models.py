from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')


class Brand(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
    size = models.ManyToManyField('Size')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    specification = models.CharField(max_length=255)


class Size(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')
