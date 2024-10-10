from os import getenv as environmental_var

# Application-run config
DEBUG = True
DEFAULT_PORT = 4000

# Database config
DB_HOST = 'ep-dark-field-a2x8dnvu.eu-central-1.aws.neon.tech'
DB_NAME = 'task_database'
DB_USER = "task_database_owner" #environmental_var("db_usr")
DB_PASSWORD = "7DozN5UjTPnh" #environmental_var("db_pwd")

#IMAGE Cloud configuration
CLOUD_NAME = "dfoevvd0s"
CLOUD_API_KEY = "755354744751921"
CLOUD_SECRET = "FyQANkrHXWULDH2ZBZJSFtenJV4"

# Paths configuration
PHOTOS_FOLDER_PATH = "/task_photos/"