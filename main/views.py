from django.shortcuts import render, HttpResponse
from items.models import Items


def index(request):
    items = Items.objects.all().order_by('-date')[:3]
    context = {
        'title': 'Непокупайэто',
        'aside': True,
        'items': items
    }
    return render(request, 'main/newindex.html', context)


def catalog(request):
    context = {
        'title': 'Категории товаров',
        'aside': False
    }
    return render(request, 'main/catalog.html', context)
