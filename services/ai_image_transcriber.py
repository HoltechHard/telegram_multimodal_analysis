import base64
from pathlib import Path


class AIImageTranscriber:
    """
    Responsible for sending images to an AI model
    and returning textual description/transcription.
    """

    def __init__(self, api_client):
        self.api_client = api_client

    def _encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    async def transcribe(self, image_path: str) -> str:
        """
        Sends image to AI model and returns transcription text.
        """

        encoded_image = self._encode_image(image_path)

        # Example generic AI call
        response = await self.api_client.describe_image(encoded_image)

        return response
    