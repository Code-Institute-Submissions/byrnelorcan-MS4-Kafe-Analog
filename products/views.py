from django.shortcuts import render, get_object_or_404
from .models import Products


# Create your views here.
def all_products(request):
    """ A view that renders all products page """

    products = Products.objects.all()

    context = {
        'products': products,
    }

    product_page = 'products/products.html'
    return render(request, product_page, context)


def product_detail(request, product_id):
    """ A view for individual product """

    product = get_object_or_404(Products, product_id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
