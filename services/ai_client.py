import requests
from config.settings import LLM_API_KEY, LLM_URL

class AIClient:
    """
    Connects to NVIDIA integrated API for Kimi-k2.5 model.
    """

    def __init__(self):
        self.api_key = LLM_API_KEY
        self.invoke_url = LLM_URL

    async def describe_image(self, image_b64: str) -> str:
        """
        Sends image to NVIDIA API and returns description.
        """
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }

        payload = {
            "model": "moonshotai/kimi-k2.5",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Transcribe the text and describe the content of this image accurately."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_b64}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 1024,
            "temperature": 0.2,
            "top_p": 0.7,
            "stream": False
        }

        try:
            # We use synchronous requests here for simplicity as per user example, 
            # but in a real async app, httpx would be better.
            # However, for this task, I will stick to the user's preferred library pattern.
            response = requests.post(self.invoke_url, headers=headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            description = result['choices'][0]['message']['content']
            return description

        except Exception as e:
            return f"Error connecting to AI API: {str(e)}"
    