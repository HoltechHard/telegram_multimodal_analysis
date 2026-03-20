from telethon import TelegramClient, events

from config.settings import (
    API_ID,
    API_HASH,
    SESSION_NAME,
    CHANNEL_USERNAME
)


class TelegramListener:
    """
    Responsible ONLY for:
    - Telegram connection lifecycle
    - Event subscription
    - Delegating events to handler
    """

    def __init__(self, message_handler):
        self.client = TelegramClient(
            SESSION_NAME,
            API_ID,
            API_HASH
        )

        # Dependency Injection
        self.handler = message_handler

    async def start(self):

        @self.client.on(events.NewMessage(chats=CHANNEL_USERNAME))
        async def new_message_listener(event):
            await self.handler.process(event)

        await self.client.start()

        print("Listening for multimodal posts...")
        await self.client.run_until_disconnected()
        