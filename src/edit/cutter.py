import ffmpeg
import logging
import os

logger = logging.getLogger(__name__)

class VideoCutter:
    def __init__(self):
        pass

    def cut_clip(self, input_path: str, start_time: str, end_time: str, output_path: str):
        """
        Cuts a clip from the video/audio file.
        Note: If input is audio-only, this will produce an audio clip.
        If we want video, we assume input_path is a video file.
        For the podcast bot, we download audio (mp3). 
        If we want to make a video for Reels, we need a background image or video.
        
        For this MVP, let's assume we might be cutting the downloaded audio 
        and then later combining it with a static image to make a video.
        """
        logger.info(f"Cutting clip from {start_time} to {end_time}...")
        try:
            (
                ffmpeg
                .input(input_path, ss=start_time, to=end_time)
                .output(output_path, c='copy') # Fast cut without re-encoding if possible
                .overwrite_output()
                .run(quiet=True)
            )
            logger.info(f"Clip saved to {output_path}")
            return output_path
        except ffmpeg.Error as e:
            logger.error(f"Error cutting clip: {e.stderr.decode('utf8')}")
            raise
