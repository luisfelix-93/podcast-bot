import ffmpeg
import logging
import os

logger = logging.getLogger(__name__)

class VideoRenderer:
    def __init__(self):
        pass

    def render_video(self, audio_path: str, image_path: str, srt_path: str, output_path: str):
        """
        Combines audio, a static background image, and subtitles into a vertical video (9:16).
        """
        logger.info(f"Rendering video to {output_path}...")
        
        try:
            # Input streams
            audio = ffmpeg.input(audio_path)
            image = ffmpeg.input(image_path, loop=1)
            
            # Video settings for 9:16 (e.g., 1080x1920)
            # We assume the image is already 1080x1920 or we scale it.
            
            stream = ffmpeg.output(
                image, 
                audio, 
                output_path,
                vcodec='libx264',
                acodec='aac',
                pix_fmt='yuv420p',
                shortest=None, # Stop when shortest input ends (audio)
                vf=f"subtitles={srt_path}:force_style='Alignment=2,Fontsize=24,MarginV=70'", # Simple subtitle style
                t=self._get_duration(audio_path) # Explicit duration to match audio
            )
            
            stream.overwrite_output().run(quiet=True)
            logger.info("Video rendering complete.")
            return output_path
            
        except ffmpeg.Error as e:
            logger.error(f"Error rendering video: {e.stderr.decode('utf8') if e.stderr else str(e)}")
            raise

    def _get_duration(self, file_path: str) -> float:
        try:
            probe = ffmpeg.probe(file_path)
            return float(probe['format']['duration'])
        except Exception:
            return 0.0
