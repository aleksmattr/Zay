
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    text = models.TextField()

class Slider(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img')

