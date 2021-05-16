from django.db import models
from django.conf import settings
from django.forms import Select
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):

    choices = [('m', 'Мужской пол'), ('f', 'Женский пол')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="avatars/%Y/%m/%d", default="avatars/default.png")

    def __str__(self):
        return f"Профиль пользователя {self.user.username}."
# автоматическое обновление модели Profile при изменении User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()