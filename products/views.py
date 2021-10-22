from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Products


# Create your views here.
def all_products(request):
    """ A view that renders all products page """

    products = Products.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search?")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) 
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    product_page = 'products/products.html'
    return render(request, product_page, context)


def product_detail(request, product_id):
    """ A view for individual product """

    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
