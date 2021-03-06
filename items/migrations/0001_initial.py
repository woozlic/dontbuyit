# Generated by Django 3.1.5 on 2021-05-17 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'unique_together': {('category_name',)},
            },
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=80, verbose_name='Подкатегория')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='items.categories')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('title', models.CharField(max_length=200, verbose_name='Название товара')),
                ('image_1', models.ImageField(upload_to='items/%Y/%m/%d', verbose_name='Фотография товара 1')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='items/%Y/%m/%d', verbose_name='Фотография товара 2')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='items/%Y/%m/%d', verbose_name='Фотография товара 3')),
                ('deposit', models.FloatField(verbose_name='Залог')),
                ('full_price', models.FloatField(verbose_name='Полная цена вещи')),
                ('cost', models.FloatField(verbose_name='Цена')),
                ('text', models.TextField(verbose_name='Полное описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('period', models.CharField(default='3 дня', max_length=80, verbose_name='Период')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.categories')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.subcategories', verbose_name='Подкатегория')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
