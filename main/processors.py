from .models import Category

def all_link(request):
    links = Category.objects.all()
    return dict(links=links)