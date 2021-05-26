from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from chat.models import Room
from django.contrib.auth.models import User
from django.core import serializers


@login_required
def chat_index(request):
    return render(request, 'chat/chat_index.html')


@login_required
def room(request, first=None, second=None):
    me = first
    other = second
    try:
        first_user = User.objects.get(pk=int(first))
        second_user = User.objects.get(pk=int(second))
        if first_user and second_user and first_user != second_user:
            room_name_1 = f'{first_user.pk}_{second_user.pk}'
            room_name_2 = f'{second_user.pk}_{first_user.pk}'
            try:
                chat_room = Room.objects.get(label=room_name_1)
                room_name = room_name_1

            except Room.DoesNotExist:
                try:
                    chat_room = Room.objects.get(label=room_name_2)
                    room_name = room_name_2

                except Room.DoesNotExist:
                    chat_room = Room(label=room_name_1)
                    room_name = room_name_1
                    chat_room.save()

            chat_room.users.add(first_user)
            chat_room.users.add(second_user)

            if first_user == request.user:
                me = first_user
                other = second_user
            elif second_user == request.user:
                me = second_user
                other = first_user

            chat_messages = reversed(chat_room.messages.order_by('-timestamp')[:50])

            rooms = serializers.serialize('json', me.rooms.all(), use_natural_foreign_keys=True)

            context = {
                'room_name': room_name,
                'room': chat_room,
                'rooms': rooms,
                'chat_messages': chat_messages,
                'me': me,
                'other': other,
            }
            return render(request, 'chat/room.html', context)
    except TypeError:
        return render(request, 'chat/room.html', {})
