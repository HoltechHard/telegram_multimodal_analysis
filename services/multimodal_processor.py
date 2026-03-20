class MultimodalProcessor:

    def __init__(self, transcriber):
        self.transcriber = transcriber

    async def build_multimodal_caption(self, image_path, caption):
        """
        Takes the AI transcription result and concatenates it with the 
        original Telegram post caption.
        """

        # 1. Get transcription from AI
        ai_text = await self.transcriber.transcribe(image_path)

        # 2. Handle empty caption
        original_caption = caption or ""

        # 3. Concatenate (AI transcription first, then original caption)
        # As requested: "the multimodal caption need to return the image transcription text 
        # together with the caption text in the same variable."
        
        # We'll use a clear separator for readability, but keep them in the same variable.
        multimodal_result = f"[AI TRANSCRIPTION]: {ai_text}\n\n[ORIGINAL CAPTION]: {original_caption}"

        return multimodal_result.strip()