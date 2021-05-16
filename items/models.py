from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from pytils.translit import slugify

from django.db.models.signals import pre_save
from django.dispatch import receiver


class CategoriesManager(models.Manager):
    def get_by_natural_key(self, category_name):
        return self.get(category_name=category_name)


class Categories(models.Model):
    category_name = models.CharField('Категория', max_length=80, unique=True)

    objects = CategoriesManager()

    def __str__(self):
        return self.category_name

    class Meta:
        unique_together = [['category_name']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategories(models.Model):
    subcategory_name = models.CharField('Подкатегория', max_length=80)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory')

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Items(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Пользователь')
    slug = models.SlugField(max_length=200, blank=True)
    title = models.CharField("Название товара", max_length=200)
    image = models.ImageField(upload_to="items/%Y/%m/%d", verbose_name='Фотография товара')
    # category = models.CharField("Категория", max_length=80, default="Прочее")
    # sub_category = models.CharField("Подкатегория", max_length=80, default="Другое")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name='Подкатегория')
    cost = models.FloatField("Цена")
    text = models.TextField("Полное описание")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    period = models.CharField("Период", max_length=80, default="3 дня")

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


@receiver(pre_save, sender=Items)
def save_category_after_subcategory(sender, instance, **kwargs):
    instance.category = instance.subcategory.category



