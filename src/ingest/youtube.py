import os
import logging
import yt_dlp
from typing import Optional

logger = logging.getLogger(__name__)

class YouTubeDownloader:
    def __init__(self, output_dir: str = "downloads", cookies_path: Optional[str] = None):
        self.output_dir = output_dir
        self.cookies_path = cookies_path
        os.makedirs(output_dir, exist_ok=True)

    def download(self, url: str) -> Optional[str]:
        """
        Downloads audio from a YouTube video.
        Returns the path to the downloaded file.
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(self.output_dir, '%(id)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
        }

        if self.cookies_path:
            ydl_opts['cookiefile'] = self.cookies_path

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                logger.info(f"Downloading {url}...")
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                # yt-dlp changes extension after post-processing
                final_filename = os.path.splitext(filename)[0] + ".mp3"
                
                if os.path.exists(final_filename):
                    logger.info(f"Download complete: {final_filename}")
                    return final_filename
                else:
                    logger.error(f"File not found after download: {final_filename}")
                    return None
        except Exception as e:
            logger.error(f"Error downloading {url}: {e}")
            return None

    def get_video_info(self, url: str) -> Optional[dict]:
        """
        Extracts metadata from a YouTube video without downloading.
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        if self.cookies_path:
            ydl_opts['cookiefile'] = self.cookies_path

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            logger.error(f"Error getting info for {url}: {e}")
            return None

    def get_latest_video_from_channel(self, channel_url: str) -> Optional[str]:
        """
        Gets the URL of the latest video from a channel.
        """
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
            'playlistend': 1,
            'sort': 'date', # Ensure we get the latest
        }

        if self.cookies_path:
            ydl_opts['cookiefile'] = self.cookies_path

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                logger.info(f"Fetching latest video from {channel_url}...")
                info = ydl.extract_info(channel_url, download=False)
                
                if 'entries' in info and info['entries']:
                    latest_video = info['entries'][0]
                    video_id = latest_video.get('id')
                    if video_id:
                        return f"https://www.youtube.com/watch?v={video_id}"
                
                logger.error("No videos found in channel.")
                return None
        except Exception as e:
            logger.error(f"Error getting latest video from {channel_url}: {e}")
            return None
