from items.models import Items


def run():
    all_objects = Items.objects.all()
    if all_objects:
        for obj in all_objects:
            obj.save()
        print('All objects saved')
    else:
        print('There is no objects to save')
