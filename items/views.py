from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, Categories, SubCategories
from .forms import ItemsForm, SearchForm
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity


class ItemDetailView(DetailView):
    model = Items
    template_name = "items/item_detail.html"
    context_object_name = 'item'
    extra_context = {'aside': True}


def show_item(request, category, subcategory, slug, pk):
    item = get_object_or_404(Items, pk=pk)
    context = {'item': item, 'aside': True}
    return render(request, 'items/item_detail.html', context)


def edit_item(request, category, subcategory, slug, pk):
    item = get_object_or_404(Items, pk=pk)
    context = {'item': item, 'aside': True}
    return render(request, 'items/edit_item.html', context)


def show_item_other(request, category, slug, pk):
    item = get_object_or_404(Items, pk=pk)
    context = {'item': item, 'aside': True}
    return render(request, 'items/item_detail.html', context)


def load_subcategories(request):
    category = request.GET.get('category')
    subcategories = SubCategories.objects.filter(category__id=category).order_by('subcategory_name')
    return render(request, 'items/subcategories_drop_down.html', {'subcategories': subcategories})


def my_rents(request):
    rents = Items.objects.filter(user=request.user).order_by('-date')
    count = len(rents)
    rents = rents[:3]
    context = {
        'items': rents,
        'count': count
    }
    return render(request, 'items/my_rents.html', context)

def all_rents(request):
    rents = Items.objects.filter(user=request.user).order_by('-date')
    count = len(rents)
    context = {
        'items': rents,
        'count': count
    }
    return render(request, 'items/all_rents.html', context)


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') +\
                SearchVector('text', weight='B')
            search_query = SearchQuery(query)
            results = Items.objects.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1).order_by('-similarity')
    context = {'form': form, 'query': query, 'items': results, 'aside':True}
    return render(request, 'items/search.html', context=context)


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
    context = {'items': items, 'aside': True}
    return render(request, "items/all.html", context)


@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ItemsForm
    context = {"aside": False, "form": form}
    return render(request, "items/add.html", context)
