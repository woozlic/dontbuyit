import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from account.models import Profile, User
from chat.models import Message, Room
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_name = ''
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
        except KeyError:
            pass
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_image(self):
        profile = Profile.objects.get(user=self.user)
        return profile.image.url

    @database_sync_to_async
    def create_message(self, message, timestamp):
        room = Room.objects.get(label=self.room_name)
        msg = Message(user=self.user, room=room, message=message, timestamp=timestamp)
        msg.save()
        return msg

    # Receive message from WebSocket
    async def receive(self, text_data):
        now = timezone.now()
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        image_url = await self.get_image()
        await self.create_message(message, now)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
                'image_url': image_url,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
