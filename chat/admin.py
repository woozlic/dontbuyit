from django.contrib import admin
from .models import Message, Room

admin.site.register(Message)
admin.site.register(Room)

# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
#     fields = ('user', 'room', 'message', 'timestamp')
#     list_display = ['user', 'room', 'message', 'timestamp']
#
#
# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ['label']
