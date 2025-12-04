import pytest
from unittest.mock import MagicMock, patch
from src.edit.cutter import VideoCutter

def test_cut_clip_success(mock_env):
    with patch('src.edit.cutter.ffmpeg') as mock_ffmpeg:
        # Setup mock
        mock_input = MagicMock()
        mock_ffmpeg.input.return_value = mock_input
        mock_output = MagicMock()
        mock_input.output.return_value = mock_output
        
        cutter = VideoCutter()
        cutter.cut_clip("input.mp3", "00:00:10", "00:00:20", "output.mp3")
        
        # Verify
        mock_ffmpeg.input.assert_called_with("input.mp3", ss="00:00:10", to="00:00:20")
        mock_output.run.assert_called_once()

def test_cut_clip_failure(mock_env):
    with patch('src.edit.cutter.ffmpeg') as mock_ffmpeg:
        # Setup mock to raise exception
        mock_ffmpeg.input.side_effect = Exception("FFmpeg Error")
        
        cutter = VideoCutter()
        with pytest.raises(Exception):
            cutter.cut_clip("input.mp3", "00:00:10", "00:00:20", "output.mp3")
