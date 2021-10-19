from django.contrib import admin
from .models import Coffee, Category, Genre, Vinyl, Condition

# Register your models here.


class VinylAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',
        'name',
        'artist',
        'category',
        'price',
        'image',
        'in_stock',
    )

    ordering = ('product_id',)

class CoffeeAdmin(admin.ModelAdmin):
    list_display = (
        'product_id',
        'name',
        'category',
        'price',
        'image',
        'in_stock',
    )

    ordering = ('product_id',)


admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Vinyl, VinylAdmin)
admin.site.register(Condition)
