import pytest
import os
import sys

# Add src to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Force utf-8 encoding for stdout/stderr
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_API_KEY", "test_key")
    monkeypatch.setenv("TELEGRAM_TOKEN", "test_token")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "123456")
    monkeypatch.setenv("R2_ACCESS_KEY", "test_access")
    monkeypatch.setenv("R2_SECRET_KEY", "test_secret")
    monkeypatch.setenv("R2_BUCKET_NAME", "test_bucket")
    monkeypatch.setenv("R2_ENDPOINT_URL", "https://test.r2.cloudflarestorage.com")
