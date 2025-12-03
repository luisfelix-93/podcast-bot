import os
from typing import Dict, Any, List

class SRTGenerator:
    @staticmethod
    def format_timestamp(seconds: float) -> str:
        """Converts seconds to SRT timestamp format (HH:MM:SS,mmm)."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

    @staticmethod
    def generate_srt(transcription_result: Dict[str, Any], output_path: str):
        """
        Generates an SRT file from the transcription result.
        """
        segments = transcription_result.get('segments', [])
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(segments, start=1):
                start = SRTGenerator.format_timestamp(segment['start'])
                end = SRTGenerator.format_timestamp(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{text}\n\n")

    @staticmethod
    def get_segments_within_range(transcription_result: Dict[str, Any], start_time: float, end_time: float) -> List[Dict[str, Any]]:
        """
        Extracts segments that fall within a specific time range.
        Useful for creating SRTs for clips.
        """
        segments = transcription_result.get('segments', [])
        relevant_segments = []
        
        for segment in segments:
            # Check if segment overlaps with the range
            seg_start = segment['start']
            seg_end = segment['end']
            
            if seg_end > start_time and seg_start < end_time:
                # Adjust timestamps relative to the clip start
                adjusted_start = max(0, seg_start - start_time)
                adjusted_end = min(end_time - start_time, seg_end - start_time)
                
                relevant_segments.append({
                    'start': adjusted_start,
                    'end': adjusted_end,
                    'text': segment['text']
                })
                
        return relevant_segments

    @staticmethod
    def generate_srt_for_clip(segments: List[Dict[str, Any]], output_path: str):
        """Generates SRT for a specific list of segments."""
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(segments, start=1):
                start = SRTGenerator.format_timestamp(segment['start'])
                end = SRTGenerator.format_timestamp(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{text}\n\n")
