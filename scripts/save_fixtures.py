from items.models import Items, Categories, SubCategories


def run():
    """Save all objects to update fixtures"""

    all_objects = Items.objects.all()
    if all_objects:
        for obj in all_objects:
            obj.save()
        print('All items saved')
    else:
        print('There is no items to save')

    all_categories = Categories.objects.all()
    if all_categories:
        for category in all_categories:
            category.save()
        print('All categories saved')
    else:
        print('There is no categories to save')

    all_subcategories = SubCategories.objects.all()
    if all_subcategories:
        for subcategory in all_subcategories:
            subcategory.save()
        print('All subcategories saved')
    else:
        print('There is no subcategories to save')
