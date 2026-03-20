class MultimodalProcessor:

    def __init__(self, transcriber):
        self.transcriber = transcriber

    async def build_multimodal_caption(self, image_path, caption):

        ai_text = await self.transcriber.transcribe(image_path)

        multimodal_caption = f"""
CAPTION:
{caption}

IMAGE TRANSCRIPTION:
{ai_text}
"""

        return multimodal_caption