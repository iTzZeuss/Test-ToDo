import os

# Run config
DEBUG = True
DEFAULT_PORT = 4000

# Database config
DB_HOST = os.getenv('db_url')

# Paths configuration
PHOTOS_FOLDER_PATH = "task_photos/"