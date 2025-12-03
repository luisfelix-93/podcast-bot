import logging
import asyncio
from telegram import Bot
from telegram.error import TelegramError

logger = logging.getLogger(__name__)

class TelegramNotifier:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=token)

    async def send_message(self, message: str):
        """Sends a text message to the configured chat."""
        logger.info(f"Sending Telegram message: {message}")
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=message)
        except TelegramError as e:
            logger.error(f"Failed to send Telegram message: {e}")

    async def send_video(self, video_path: str, caption: str = ""):
        """Sends a video file to the configured chat."""
        logger.info(f"Sending video {video_path} to Telegram...")
        try:
            with open(video_path, 'rb') as video_file:
                await self.bot.send_video(chat_id=self.chat_id, video=video_file, caption=caption)
        except TelegramError as e:
            logger.error(f"Failed to send video: {e}")
        except FileNotFoundError:
            logger.error(f"Video file not found: {video_path}")

    def send_message_sync(self, message: str):
        """Synchronous wrapper for sending message."""
        asyncio.run(self.send_message(message))

    def send_video_sync(self, video_path: str, caption: str = ""):
        """Synchronous wrapper for sending video."""
        asyncio.run(self.send_video(video_path, caption))
