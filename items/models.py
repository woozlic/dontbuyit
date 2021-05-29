from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from pytils.translit import slugify
import logging
logger = logging.getLogger(__name__)


class CategoriesManager(models.Manager):
    def get_by_natural_key(self, category_name):
        return self.get(category_name=category_name)


class Categories(models.Model):
    category_name = models.CharField('Категория', max_length=80, unique=True, blank=False)
    category_slug = models.SlugField('Slug', blank=True)

    objects = CategoriesManager()

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = [['category_name']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategories(models.Model):
    subcategory_name = models.CharField('Подкатегория', max_length=80, blank=False)
    subcategory_slug = models.SlugField('Slug', blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory')

    def __str__(self):
        return self.subcategory_name

    def save(self, *args, **kwargs):
        if not self.subcategory_slug:
            self.subcategory_slug = slugify(self.subcategory_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Items(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, verbose_name='Пользователь')
    slug = models.SlugField(max_length=200, blank=True)
    title = models.CharField("Название товара", max_length=200)
    image_1 = models.ImageField(upload_to="items/%Y/%m/%d", verbose_name='Фотография товара 1')
    image_2 = models.ImageField(upload_to="items/%Y/%m/%d", verbose_name='Фотография товара 2', null=True, blank=True)
    image_3 = models.ImageField(upload_to="items/%Y/%m/%d", verbose_name='Фотография товара 3', null=True, blank=True)
    deposit = models.FloatField("Залог")
    full_price = models.FloatField("Полная цена вещи")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
    category_slug = models.SlugField(max_length=200, blank=True)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='Подкатегория')
    subcategory_slug = models.SlugField(max_length=200, blank=True)
    cost = models.FloatField("Цена")
    text = models.TextField("Полное описание")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    period = models.CharField("Период", max_length=80, default="1 сутки", choices=[
        ('1 час', '1 час'), ('1 сутки', '1 сутки'), ('3 суток', '3 суток'), ('7 суток', '7 суток'),
        ('1 месяц', '1 месяц')])

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.category and self.subcategory:
            self.category = self.subcategory.category
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.category_slug:
            self.category_slug = slugify(self.category.category_name)
        if self.subcategory and not self.subcategory_slug:
            self.subcategory_slug = slugify(self.subcategory.subcategory_name)
        super(Items, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'






