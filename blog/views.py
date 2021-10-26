from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Blog

@login_required
def all_blogs(request):
    """ View to show all blogs """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('login'))

    blog = Blog.objects.all()

    context = {
        'blog': blog
    }

    return render(request, 'blog/blog.html', context)

def blog_detail(request, blog_id):
    """ A view for individual blog """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)