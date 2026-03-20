# System Documentation: Telegram Multimodal Extraction

This system is designed to automatically capture images and captions from a specified Telegram channel, process the image using a vision AI model (Kimi-k2.5), and generate a combined multimodal caption.

## Component Overview

The system follows a modular architecture based on SOLID principles, specifically focusing on Single Responsibility and Dependency Injection.

### 1. Core Layer (Infrastructure)
- **TelegramListener (`core/telegram_client.py`)**: Responsible for connecting to Telegram using Telethon. It listens for `NewMessage` events on a specific channel and delegates processing to the `MessageHandler`.
- **MessageHandler (`core/message_handler.py`)**: Acts as a controller. It receives the event, extracts basic data, and orchestrates the download and processing flow.

### 2. Services Layer (Business Logic)
- **MediaDownloader (`services/media_downloader.py`)**: Handles the physical download of images from Telegram. It generates deterministic filenames based on message IDs and timestamps.
- **AIClient (`services/ai_client.py`)**: Communicates with the NVIDIA Integrated API. Specifically, it sends requests to the `moonshotai/kimi-k2.5` model, including base64 encoded images.
- **AIImageTranscriber (`services/ai_image_transcriber.py`)**: A wrapper around `AIClient` that handles image encoding (conversion to Base64) and prepares the transcription request.
- **MultimodalProcessor (`services/multimodal_processor.py`)**: The final processing stage. It takes the AI-generated transcription and concatenates it with the original Telegram caption, ensuring a unified result.

## Data Flow (Whole Component Interaction)

1.  **Event Capture**: `TelegramListener` detects a new message with a photo for the target channel.
2.  **Delegation**: The listener calls `MessageHandler.process(event)`.
3.  **Download**: `MessageHandler` asks `MediaDownloader` to save the image locally.
4.  **Processing**:
    - `MessageHandler` calls `MultimodalProcessor.build_multimodal_caption`.
    - `MultimodalProcessor` calls `AIImageTranscriber.transcribe`.
    - `AIImageTranscriber` encodes the image to Base64 and calls `AIClient.describe_image`.
    - `AIClient` makes an API call to NVIDIA's Kimi-k2.5 model.
5.  **Concatenation**: `MultimodalProcessor` receives the transcription, combines it with the original caption (if any), and returns the final string.
6.  **Output**: `MessageHandler` prints the result to the console showing the image path and the combined multimodal caption.

## Connection Details
- **Model**: `moonshotai/kimi-k2.5`
- **Endpoint**: `https://integrate.api.nvidia.com/v1/chat/completions`
- **API Key**: Configured in `config/settings.py` via `NVIDIA_API_KEY`.
