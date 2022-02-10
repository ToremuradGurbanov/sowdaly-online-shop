from django.http import HttpResponse
from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from main.models import Category
from .models import Product


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_total = products.count()

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        product_total = products.count()
        
    context = {
        'products': paged_products,
        'product_total': product_total,
        'categories': categories,
    }
    template_name = 'store/store.html'
    return render(request, template_name, context)



def product_detail(request, category_slug, product_slug):
    template_name = 'store/product_detail.html'
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

    except Exception as e:
        raise e
    context = {
        'single_product': single_product
    }
    return render(request, template_name, context)



def search(request):
    template_name='store/store.html'
    if 'keyword'in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(product_name__icontains=keyword)
            product_total = products.count()
    context = {'products':products, 'product_total':product_total}    

    return render(request, template_name, context)