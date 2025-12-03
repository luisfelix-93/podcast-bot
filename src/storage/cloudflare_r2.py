import boto3
import logging
import os
from botocore.exceptions import NoCredentialsError

logger = logging.getLogger(__name__)

class R2Uploader:
    def __init__(self, access_key: str, secret_key: str, bucket_name: str, endpoint_url: str):
        self.bucket_name = bucket_name
        self.s3 = boto3.client(
            's3',
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name='auto' # Cloudflare R2 uses 'auto'
        )

    def upload_file(self, file_path: str, object_name: str = None) -> str:
        """
        Uploads a file to Cloudflare R2.
        Returns the public URL (assuming public bucket or just the key).
        """
        if object_name is None:
            object_name = os.path.basename(file_path)

        logger.info(f"Uploading {file_path} to R2 bucket {self.bucket_name} as {object_name}...")
        
        try:
            self.s3.upload_file(file_path, self.bucket_name, object_name)
            logger.info("Upload successful.")
            # Return a constructed URL (adjust based on your R2 public domain setup)
            # For now, returning the object key or a standard R2 URL structure
            return f"https://{self.bucket_name}.r2.cloudflarestorage.com/{object_name}" 
        except FileNotFoundError:
            logger.error(f"The file was not found: {file_path}")
            return None
        except NoCredentialsError:
            logger.error("Credentials not available")
            return None
        except Exception as e:
            logger.error(f"Upload failed: {e}")
            return None
