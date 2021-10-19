from django.shortcuts import render
from .models import Vinyl

# Create your views here.


def all_vinyl(request):
    """ A view that renders all products page """

    vinyls = Vinyl.objects.all()

    context = {
        'vinyls': vinyls,
    }

    return render(request, 'products/vinyls.html', context)
