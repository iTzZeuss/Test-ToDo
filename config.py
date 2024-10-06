from os import getenv as environmental_var

# Run config
DEBUG = True
DEFAULT_PORT = 4000

# Database config
DB_HOST = 'ep-dark-field-a2x8dnvu.eu-central-1.aws.neon.tech'
DB_NAME = 'task_database'
DB_USER = 'task_database_owner'
DB_PASSWORD = environmental_var("db_pwd")

# Paths configuration
PHOTOS_FOLDER_PATH = "task_photos/"