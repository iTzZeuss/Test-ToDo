import os

# Run config
DEBUG = True
DEFAULT_PORT = 4000

# Database config
DB_HOST = 'dpg-cs01lmpu0jms73e05tfg-a.frankfurt-postgres.render.com'
DB_NAME = 'tasks_db_0fry'
DB_USER = 'tasks_db_0fry_user'
DB_PASSWORD = os.getenv('db_password')
DEBUG_DB_PASSWORD = '0BmyfK6LYgtJ1L1e6tpZMrU2I74uPE53' #when debug is finished delete it
DB_PORT = 5432

# Paths configuration
PHOTOS_FOLDER_PATH = "static/photos/"