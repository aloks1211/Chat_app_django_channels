from channels.consumer import AsyncConsumer
import asyncio
import json

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        """

        :param event:
        :return:
        """
        print("connected", event)
        await self.send({
            "type": 'websocket.accept',
        })

    async def websocket_receive(self, event):
        """

        :param event:
        :return:
        """
        print("received", event)
        event_text = event.get('text', None)
        if event_text is not None:
            loaded_data = json.loads(event_text)
            msg = loaded_data.get('message')
            await self.send({
                "type": 'websocket.send',
                "text": msg
            })

    async def websocket_disconnect(self, event):
        """

        :param event:
        :return:
        """
        print("disconnected", event)
