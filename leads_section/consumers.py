import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notifications_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications_group", self.channel_name)

    async def receive(self, text_data):
        # Handle incoming messages from the client
        data = json.loads(text_data)

        # Check for a ping message and send pong to keep connection alive
        if data.get("type") == "ping":
            await self.send(text_data=json.dumps({"type": "pong"}))
        else:
            # Handle notification message
            message = data.get("message")
            await self.send(text_data=json.dumps({"message": message}))

    async def send_notification(self, event):
        # Send notification message to WebSocket
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))


class LeadNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "lead_notifications"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        # Handle incoming messages from the client
        data = json.loads(text_data)

        # Check for a ping message and send pong to keep connection alive
        if data.get("type") == "ping":
            await self.send(text_data=json.dumps({"type": "pong"}))
        else:
            # No need to handle specific messages here for this consumer
            pass

    async def send_notification(self, event):
        # Send notification message to WebSocket
        await self.send(text_data=json.dumps(event["message"]))
