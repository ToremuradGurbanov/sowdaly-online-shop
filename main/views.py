from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
    template_name='main/home.html'
    context = {
        'products': products
    }
    return render(request, template_name, context)