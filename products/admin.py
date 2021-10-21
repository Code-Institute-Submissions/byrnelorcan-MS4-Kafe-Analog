from django.contrib import admin
from .models import Products, Category, Genre, Condition

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',
        'category',
        'name',
        'artist',
        'price',
        'image',
        'in_stock',
    )

    ordering = ('product_id',)


admin.site.register(Products, ProductAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Condition)
