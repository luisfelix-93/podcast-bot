import json
import os

class PromptEngineer:
    def __init__(self):
        self.base_prompt = """
        Analyze the following podcast transcript and identify 3 to 5 viral clips suitable for TikTok, Reels, and Shorts (30-60 seconds).
        
        Criteria for viral clips:
        1. High emotional engagement (humor, shock, inspiration, anger).
        2. Standalone value (makes sense without context).
        3. Strong hook in the first 3 seconds.
        4. Relatable content or practical advice.

        Return the result strictly in the following JSON format:
        {
            "clips": [
                {
                    "start_time": "HH:MM:SS",
                    "end_time": "HH:MM:SS",
                    "title": "Catchy Title for the Clip",
                    "description": "Short description for social media caption",
                    "category": "humor|motivation|controversial|educational",
                    "virality_score": 0.9,
                    "reason": "Why this clip is viral"
                }
            ]
        }
        
        Ensure timestamps are accurate and match the transcript flow.
        """

    def get_analysis_prompt(self) -> str:
        return self.base_prompt
