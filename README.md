# PodBot 🎙️✂️

Automated podcast clipper that monitors YouTube, identifies viral moments using AI, cuts them into vertical videos, and uploads them to the cloud.

## 🚀 Features

- **Automated Ingestion**: Downloads podcasts from YouTube.
- **AI Analysis**: Uses DeepSeek to find viral moments (funny, emotional, controversial).
- **Smart Editing**: Cuts video/audio, generates thumbnails, and (optionally) burns subtitles.
- **Cloud Storage**: Uploads clips to Cloudflare R2 (Free Tier friendly).
- **Notifications**: Sends new clips directly to Telegram.
- **GitHub Actions**: Runs daily automatically.

## 🛠️ Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/pod-bot.git
   cd pod-bot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Secrets**
   Create a `.env` file (see `docs/setup.md` for details) with your API keys:
   - `DEEPSEEK_API_KEY`
   - `TELEGRAM_TOKEN`
   - `R2_ACCESS_KEY`...

4. **Run Manually**
   ```bash
   python src/main.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

## 📚 Documentation

- [Setup Guide](docs/setup.md): Detailed configuration instructions.
- [Requirements](docs/requirements.md): Project goals and scope.

## 🤖 Tech Stack

- **Python 3.11**
- **yt-dlp** (Download)
- **Whisper** (Transcription)
- **DeepSeek** (Analysis)
- **FFmpeg** (Editing)
- **Cloudflare R2** (Storage)
