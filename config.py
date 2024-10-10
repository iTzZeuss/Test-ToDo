from os import getenv as environmental_var

# Application-run config
DEBUG = True
DEFAULT_PORT = 4000

# Database config
DB_HOST = 'ep-dark-field-a2x8dnvu.eu-central-1.aws.neon.tech'
DB_NAME = 'task_database'
DB_USER = environmental_var("db_usr")
DB_PASSWORD = environmental_var("db_pwd")

# Paths configuration
PHOTOS_FOLDER_PATH = "/task_photos/"