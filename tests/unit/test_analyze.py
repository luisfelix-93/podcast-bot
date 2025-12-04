import pytest
from unittest.mock import MagicMock, patch
from src.analyze.deepseek_client import DeepSeekClient

def test_analyze_success(mock_env):
    with patch('src.analyze.deepseek_client.requests.post') as mock_post:
        # Setup mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{
                'message': {
                    'content': '{"clips": []}'
                }
            }]
        }
        mock_post.return_value = mock_response
        
        client = DeepSeekClient()
        result = client.analyze_transcript("test transcript", "test prompt")
        
        # Verify
        assert result == {'clips': []}
        mock_post.assert_called_once()

def test_analyze_failure(mock_env):
    with patch('src.analyze.deepseek_client.requests.post') as mock_post:
        # Setup mock to raise exception
        mock_post.side_effect = Exception("API Error")
        
        client = DeepSeekClient()
        with pytest.raises(Exception):
            client.analyze_transcript("test transcript", "test prompt")
