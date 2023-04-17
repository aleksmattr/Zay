from django.contrib import admin
from .models import Category, Brand, Size, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)

