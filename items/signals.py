from django.db.models.signals import pre_save, post_save, post_init, pre_init
from django.dispatch import receiver
from models import Items


# @receiver(pre_save, sender=Items)
# def save_category_after_subcategory(sender, instance, **kwargs):
#     print('qqq')
    # logger.error('qq')
    # if instance.category and instance.category.category_name == 'Разное':
    #     pass
    # else:
    #     logger.error(instance.category + instance.subcategory)
    # instance.category = instance.subcategory.category
    # instance.save()
