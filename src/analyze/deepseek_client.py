import os
import logging
import json
import requests
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

class DeepSeekClient:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        self.base_url = "https://api.deepseek.com/v1"
        
        if not self.api_key:
            logger.warning("DeepSeek API key not found. Analysis will fail.")

    def analyze_transcript(self, transcript_text: str, prompt: str) -> Dict[str, Any]:
        """
        Sends the transcript to DeepSeek for analysis.
        Returns the JSON response with identified clips.
        """
        if not self.api_key:
            raise ValueError("DeepSeek API key is missing.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are an expert video editor and social media manager. You identify viral moments in podcasts."},
                {"role": "user", "content": f"{prompt}\n\nTRANSCRIPT:\n{transcript_text}"}
            ],
            "temperature": 0.7,
            "response_format": {"type": "json_object"}
        }

        try:
            logger.info("Sending transcript to DeepSeek for analysis...")
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            # Parse JSON content
            return json.loads(content)
        except Exception as e:
            logger.error(f"Error calling DeepSeek API: {e}")
            raise
