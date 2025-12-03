# Setup Guide

## 1. Environment Setup

### Local Development
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt` (or use Poetry).
3. Install FFmpeg and add it to your PATH.
4. Create a `.env` file based on the secrets below.

### GitHub Actions
1. Go to your repository settings -> Secrets and variables -> Actions.
2. Add the following repository secrets:

## 2. Required Secrets

| Secret Name | Description |
|-------------|-------------|
| `DEEPSEEK_API_KEY` | API key for DeepSeek (AI analysis). |
| `TELEGRAM_TOKEN` | Token for your Telegram bot (from @BotFather). |
| `TELEGRAM_CHAT_ID` | Chat ID where the bot will send notifications. |
| `R2_ACCESS_KEY` | Cloudflare R2 Access Key ID. |
| `R2_SECRET_KEY` | Cloudflare R2 Secret Access Key. |
| `R2_BUCKET_NAME` | Name of your R2 bucket. |
| `R2_ENDPOINT_URL` | Endpoint URL for your R2 bucket (e.g., `https://<accountid>.r2.cloudflarestorage.com`). |

## 3. Running the Bot

### Locally
```bash
python -m src.main --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Via GitHub Actions
- The workflow runs automatically every day at 02:00 UTC.
- You can manually trigger it from the "Actions" tab.
