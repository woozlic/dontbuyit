from django.contrib import admin
from .models import Items, Categories, SubCategories
from .forms import SubCategoryChoiceField, PeriodChoiceField


class SubCategoriesInline(admin.TabularInline):
    model = SubCategories


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):

    fields = ('user', 'title', 'text', 'image_1', 'image_2', 'image_3', 'subcategory', 'deposit', 'full_price',
              'cost', 'period', 'category_slug', 'subcategory_slug')

    list_display = ['user', 'slug', 'title', 'image_1', 'image_2', 'image_3', 'deposit', 'full_price', 'category',
                    'get_subcategory', 'cost', 'period', 'date']
    list_filter = ['date']

    def get_subcategory(self, obj):
        # return ', '.join([sub.subcategory_name for sub in obj.category.subcategory.all()])
        return obj.subcategory

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'subcategory':
            return SubCategoryChoiceField(queryset=SubCategories.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     if db_field.name == 'period':
    #         return PeriodChoiceField(queryset=)
    #     return super().formfield_for_dbfield(db_field, request, **kwargs)

    get_subcategory.short_description = 'Подкатегория'
    get_subcategory.admin_order_field = 'category__subcategory'


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):

    inlines = [
        SubCategoriesInline,
    ]

    list_display = ['category_name']
    list_filter = ['category_name']


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):

    list_display = ['subcategory_name', 'get_category']
    list_filter = ['subcategory_name']

    def get_category(self, obj):
        return obj.category.category_name

    get_category.short_description = 'Категория'
