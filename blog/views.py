from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Blog

def all_blogs(request):
    """ View to show all blogs """

    blog = Blog.objects.all()

    context = {
        'blog': blog
    }

    return render(request, 'blog/blog.html', context)
