from django.shortcuts import render


def chat_index(request):
    return render(request, 'chat/chat_index.html')


def room(request, room_name):
    context = {
        'room_name': room_name
    }
    return render(request, 'chat/room.html', context)
