import pytest
from unittest.mock import MagicMock, patch
from src.storage.cloudflare_r2 import R2Uploader

def test_upload_success(mock_env):
    with patch('src.storage.cloudflare_r2.boto3.client') as mock_boto:
        # Setup mock
        mock_s3 = MagicMock()
        mock_boto.return_value = mock_s3
        
        uploader = R2Uploader("key", "secret", "bucket", "endpoint")
        url = uploader.upload_file("test_video.mp4")
        
        # Verify
        assert url is not None
        mock_s3.upload_file.assert_called_once()

def test_upload_failure(mock_env):
    with patch('src.storage.cloudflare_r2.boto3.client') as mock_boto:
        # Setup mock to raise exception
        mock_s3 = MagicMock()
        mock_s3.upload_file.side_effect = Exception("Upload Error")
        mock_boto.return_value = mock_s3
        
        uploader = R2Uploader("key", "secret", "bucket", "endpoint")
        url = uploader.upload_file("test_video.mp4")
        
        # Verify
        assert url is None
