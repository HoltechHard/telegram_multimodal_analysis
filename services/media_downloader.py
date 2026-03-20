from pathlib import Path
from datetime import datetime


class MediaDownloader:
    """
    Responsible ONLY for downloading media from Telegram
    and storing it locally using a deterministic filename.
    """

    def __init__(self, base_folder: str = "multimedia"):
        self.base_folder = Path(base_folder)
        self.base_folder.mkdir(exist_ok=True)

    async def download(self, client, message) -> str:
        """
        Downloads image from Telegram message.

        File name format:
            messageID + date + extension

        Example:
            1254_20260320_153045.jpg
        """

        if not message.photo:
            raise ValueError("Message does not contain a photo.")

        # message metadata
        msg_id = message.id
        msg_date = message.date.strftime("%Y%m%d_%H%M%S")

        # determine extension (Telegram usually jpg)
        extension = ".jpg"

        filename = f"{msg_id}_{msg_date}{extension}"
        file_path = self.base_folder / filename

        # download media
        await client.download_media(
            message.photo,
            file=str(file_path)
        )

        return str(file_path)
    