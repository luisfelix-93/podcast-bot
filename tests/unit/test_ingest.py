import pytest
from unittest.mock import MagicMock, patch
from src.ingest.youtube import YouTubeDownloader

def test_download_success(mock_env):
    with patch('src.ingest.youtube.YoutubeDL') as mock_ydl, \
         patch('src.ingest.youtube.os.path.exists') as mock_exists:
        # Setup mock
        mock_exists.return_value = True
        instance = mock_ydl.return_value
        instance.__enter__.return_value.extract_info.return_value = {
            'id': 'test_video',
            'title': 'Test Video',
            'ext': 'mp4'
        }
        instance.__enter__.return_value.prepare_filename.return_value = "test_downloads/test_video.mp4"
        
        downloader = YouTubeDownloader(output_dir="test_downloads")
        result = downloader.download("https://youtube.com/watch?v=test")
        
        # Verify
        assert result is not None
        instance.__enter__.return_value.download.assert_called_once()

def test_download_failure(mock_env):
    with patch('src.ingest.youtube.YoutubeDL') as mock_ydl:
        # Setup mock to raise exception
        instance = mock_ydl.return_value
        instance.__enter__.return_value.download.side_effect = Exception("Download failed")
        
        downloader = YouTubeDownloader(output_dir="test_downloads")
        result = downloader.download("https://youtube.com/watch?v=test")
        
        # Verify
        assert result is None
