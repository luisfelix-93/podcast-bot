import whisper
import logging
import os
from typing import Dict, Any

logger = logging.getLogger(__name__)

class Transcriber:
    def __init__(self, model_size: str = "tiny"):
        self.model_size = model_size
        self.model = None

    def load_model(self):
        if self.model is None:
            logger.info(f"Loading Whisper model: {self.model_size}...")
            self.model = whisper.load_model(self.model_size)

    def transcribe(self, audio_path: str) -> Dict[str, Any]:
        """
        Transcribes an audio file using Whisper.
        Returns the full result dictionary.
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        self.load_model()
        
        logger.info(f"Transcribing {audio_path}...")
        try:
            result = self.model.transcribe(audio_path)
            logger.info("Transcription complete.")
            return result
        except Exception as e:
            logger.error(f"Error during transcription: {e}")
            raise
