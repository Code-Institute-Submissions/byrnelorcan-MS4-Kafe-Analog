from django.shortcuts import render
from .models import Vinyl, Coffee


# Create your views here.
def all_products(request):
    """ A view that renders all products page """

    vinyls = Vinyl.objects.all()
    coffees = Coffee.objects.all()

    context = {
        'vinyls': vinyls,
        'coffees': coffees,
    }

    product_page = 'products/products.html'
    return render(request, product_page, context)

