from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, Categories, SubCategories
from .forms import ItemsForm
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pytils.translit

class ItemDetailView(DetailView):
    model = Items
    template_name = "items/item_detail.html"
    context_object_name = 'item'
    extra_context = {'aside': True}


def show_item(request, category, subcategory, slug, pk):
    item = get_object_or_404(Items, pk=pk)
    context = {'item': item, 'aside': True}
    return render(request, 'items/item_detail.html', context)


def show_page(request, category=None, subcategory=None, page_num=1):
    # print(category, page_num)
    items = Items.objects.all().order_by('-date')
    if category:  # любая категория кроме все товары
        # items = [item for item in items if item.category_slug == category]  # берем вещи из категорий
        if subcategory:
            items = items.filter(category_slug=category, subcategory_slug=subcategory)
        else:
            items = items.filter(category_slug=category)

    paginator = Paginator(items, 6)
    try:
        items = paginator.page(page_num)
    except EmptyPage:
        return redirect('main:index')  # здесь нужно будет возвращать 404
    if category:
        category_rus = get_object_or_404(Categories, category_slug=category)
    else:
        category_rus = ''
    if subcategory:
        subcategory_rus = get_object_or_404(SubCategories, subcategory_slug=subcategory)
    else:
        subcategory_rus = ''
    context = {'items': items, 'aside': True, 'category_slug': category, 'subcategory_slug': subcategory,
               'page_num': page_num, 'category_rus': category_rus, 'subcategory_rus': subcategory_rus}
    return render(request, 'items/all.html', context)


def show_all(request):
    items = Items.objects.all().order_by('-date')
    # paginator = Paginator(items, 6)
    # try:
    #     items = paginator.page()
    context = {'items': items, 'aside': True}
    return render(request, "items/all.html", context)


@login_required
def add_item(request):
    error = ""
    if request.method == "POST":
        form = ItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ItemsForm
    context = {"aside": False, "form": form}
    return render(request, "items/add.html", context)
