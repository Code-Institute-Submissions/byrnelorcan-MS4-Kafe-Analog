from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_id',
        'blog_title',
        'blog_content'
        'image'
    )

    ordering = ('blog_id',)


admin.site.register(Blog)