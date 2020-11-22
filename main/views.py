from django.shortcuts import render, HttpResponse
from items.models import Items

# Create your views here.

def index(request):
    items = Items.objects.all().order_by('rating')[:3]
    context = {
        'title': 'Непокупай.рф',
        'aside': True,
        'items': items
    }
    return render(request, 'main/newindex.html', context)

def catalog(request):
    context = {
        'title': 'Категории товаров',
        'aside': True
    }
    return render(request, 'main/catalog.html', context)