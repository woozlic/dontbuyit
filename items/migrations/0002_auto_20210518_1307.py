# Generated by Django 3.1.5 on 2021-05-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category_slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='items',
            name='subcategory_slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='items',
            name='period',
            field=models.CharField(choices=[('1 час', '1 час'), ('1 сутки', '1 сутки'), ('3 суток', '3 суток'), ('7 суток', '7 суток'), ('1 месяц', '1 месяц')], default='1 сутки', max_length=80, verbose_name='Период'),
        ),
    ]