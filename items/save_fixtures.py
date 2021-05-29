from items.models import Items


def save_objects():
    all_objects = Items.objects.all()
    if all_objects:
        for obj in all_objects:
            obj.save()
            print('All objects saved')
        return True
    else:
        print('There is no objects to save')
        return False


if __name__ == '__main__':
    save_objects()
