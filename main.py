import asyncio

from core.telegram_client import TelegramListener
from core.message_handler import MessageHandler

from services.media_downloader import MediaDownloader
from services.ai_client import AIClient
from services.ai_image_transcriber import AIImageTranscriber
from services.multimodal_processor import MultimodalProcessor


async def main():

    # ---------------------------
    # Infrastructure Layer
    # ---------------------------
    downloader = MediaDownloader()

    # ---------------------------
    # AI Layer
    # ---------------------------
    ai_client = AIClient()
    transcriber = AIImageTranscriber(ai_client)

    multimodal_processor = MultimodalProcessor(transcriber)

    # ---------------------------
    # Application Layer
    # ---------------------------
    handler = MessageHandler(
        downloader=downloader,
        multimodal_processor=multimodal_processor
    )

    # ---------------------------
    # Telegram Layer
    # ---------------------------
    listener = TelegramListener(handler)

    await listener.start()


if __name__ == "__main__":
    asyncio.run(main())
    