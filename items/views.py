from django.shortcuts import render, redirect
from .models import Items
from .forms import ItemsForm
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class ItemDetailView(DetailView):
    model = Items
    template_name = "items/item_detail.html"
    context_object_name = 'item'
    extra_context = {'aside': True}

def show_page(request, page_num=1, category=None):
    items = Items.objects.all().order_by('-date')
    # if category == "electronic":
    #     items = [item for item in items if item.category == "electronic"]
    if category != None:
        try:
            items = [item for item in items if item.category == category]
        except:
            items = [item for item in items if item.category == "other"]
    paginator = Paginator(items, 6)
    try:
        items = paginator.page(page_num)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {'items': items, 'aside': True}
    return render(request, 'items/all.html', context)

def show_all(request):
    items = Items.objects.all().order_by('-date')
    # paginator = Paginator(items, 6)
    # try:
    #     items = paginator.page()
    context = {'items': items, 'aside': True}
    return render(request, "items/all.html", context)
def add_item(request):
    error = ""
    if request.method == "POST":
        form = ItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = f"Вы не правильно заполнили форму"
            print(form.errors)
    form = ItemsForm
    context = {"aside": False, "form": form, 'error': error}
    return render(request, "items/add.html", context)
