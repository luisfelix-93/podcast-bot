import pytest
from unittest.mock import MagicMock, patch
from src.transcribe.whisper_local import Transcriber

def test_transcribe_success(mock_env):
    with patch('src.transcribe.whisper_local.whisper') as mock_whisper, \
         patch('src.transcribe.whisper_local.os.path.exists') as mock_exists:
        # Setup mock
        mock_exists.return_value = True
        mock_model = MagicMock()
        mock_whisper.load_model.return_value = mock_model
        mock_model.transcribe.return_value = {'text': 'Test transcript'}
        
        transcriber = Transcriber(model_size="tiny")
        result = transcriber.transcribe("test_audio.mp3")
        
        # Verify
        assert result['text'] == 'Test transcript'
        mock_model.transcribe.assert_called_once_with("test_audio.mp3")

def test_transcribe_failure(mock_env):
    with patch('src.transcribe.whisper_local.whisper') as mock_whisper, \
         patch('src.transcribe.whisper_local.os.path.exists') as mock_exists:
        # Setup mock to raise exception
        mock_exists.return_value = True
        mock_whisper.load_model.side_effect = Exception("Model load failed")
        
        transcriber = Transcriber(model_size="tiny")
        with pytest.raises(Exception):
            transcriber.transcribe("test_audio.mp3")
