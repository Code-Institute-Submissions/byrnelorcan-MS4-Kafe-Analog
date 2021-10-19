from django.contrib import admin
from .models import Coffee, Category, Genre, Vinyl, Condition

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Vinyl)
admin.site.register(Condition)
