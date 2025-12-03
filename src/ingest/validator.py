import sqlite3
import logging
from datetime import datetime
import os

logger = logging.getLogger(__name__)

class PodcastValidator:
    def __init__(self, db_path: str = "podbot.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        """Initialize the SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS processed_podcasts (
                    id TEXT PRIMARY KEY,
                    url TEXT NOT NULL,
                    title TEXT,
                    processed_at TIMESTAMP,
                    status TEXT
                )
            ''')
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")

    def is_processed(self, video_id: str) -> bool:
        """Check if a video has already been processed."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT status FROM processed_podcasts WHERE id = ?', (video_id,))
            result = cursor.fetchone()
            conn.close()
            
            if result and result[0] == 'completed':
                return True
            return False
        except Exception as e:
            logger.error(f"Error checking status for {video_id}: {e}")
            return False

    def mark_as_processing(self, video_id: str, url: str, title: str):
        """Mark a video as currently processing."""
        self._update_status(video_id, url, title, 'processing')

    def mark_as_completed(self, video_id: str):
        """Mark a video as successfully completed."""
        self._update_status(video_id, None, None, 'completed')

    def mark_as_failed(self, video_id: str):
        """Mark a video as failed."""
        self._update_status(video_id, None, None, 'failed')

    def _update_status(self, video_id: str, url: str, title: str, status: str):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            now = datetime.now()
            
            if status == 'processing':
                cursor.execute('''
                    INSERT OR REPLACE INTO processed_podcasts (id, url, title, processed_at, status)
                    VALUES (?, ?, ?, ?, ?)
                ''', (video_id, url, title, now, status))
            else:
                cursor.execute('''
                    UPDATE processed_podcasts 
                    SET status = ?, processed_at = ? 
                    WHERE id = ?
                ''', (status, now, video_id))
                
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Error updating status for {video_id}: {e}")
