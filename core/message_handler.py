#from services.media_downloader import MediaDownloader


class MessageHandler:

    def __init__(self, downloader, multimodal_processor):
        self.downloader = downloader
        self.processor = multimodal_processor

    async def process(self, event):

        message = event.message

        if not message.photo:
            return

        # extract caption
        msg_text = message.text or ""

        # download image
        image_path = await self.downloader.download(
            event.client,
            message
        )

        # build multimodal caption
        multimodal_caption = await self.processor.build_multimodal_caption(
            image_path,
            msg_text
        )

        print("\n===== MULTIMODAL RESULT =====")
        print("Image Path:", image_path)
        print(multimodal_caption)
        