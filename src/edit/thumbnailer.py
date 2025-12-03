from PIL import Image, ImageDraw, ImageFont
import logging
import os
import textwrap

logger = logging.getLogger(__name__)

class ThumbnailGenerator:
    def __init__(self, width: int = 1080, height: int = 1920):
        self.width = width
        self.height = height
        # Try to load a font, fallback to default
        try:
            self.font = ImageFont.truetype("arial.ttf", 80)
        except IOError:
            self.font = ImageFont.load_default()

    def create_background(self, title: str, output_path: str):
        """
        Creates a simple background image with the title.
        In a real app, this might use a template or a downloaded image.
        """
        logger.info(f"Generating thumbnail/background for: {title}")
        
        # Create a solid color background (e.g., dark blue/purple gradient simulation)
        img = Image.new('RGB', (self.width, self.height), color=(20, 20, 40))
        draw = ImageDraw.Draw(img)
        
        # Add Title Text
        margin = 100
        offset = 400
        
        lines = textwrap.wrap(title, width=20) # Wrap text
        for line in lines:
            # Calculate text width using textbbox (newer Pillow) or textlength
            # For compatibility, let's just center roughly or use left align with margin
            draw.text((margin, offset), line, font=self.font, fill=(255, 255, 255))
            offset += 100 # Line height
            
        # Save
        img.save(output_path)
        logger.info(f"Background saved to {output_path}")
        return output_path
