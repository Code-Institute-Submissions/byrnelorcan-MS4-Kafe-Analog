from django.shortcuts import render
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

