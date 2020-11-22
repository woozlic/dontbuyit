from django.db import models
import datetime

# Create your models here.

class Items(models.Model):
    title = models.CharField("Название товара", max_length=80)
    image = models.ImageField(upload_to="items/%Y/%m/%d", blank=True)
    cost = models.FloatField("Цена")
    intro = models.CharField("Краткое описание", max_length=250)
    text = models.TextField("Полное описание")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    rating = models.FloatField("Рейтинг", default=0.0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'