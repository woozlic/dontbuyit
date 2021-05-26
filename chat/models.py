from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Room(models.Model):
    users = models.ManyToManyField(User, related_name='rooms')
    label = models.SlugField(unique=True)

    def __str__(self):
        return self.label


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Отправитель')
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"{self.user.username}: {self.message}"
