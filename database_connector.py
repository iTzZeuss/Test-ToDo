import psycopg2
import config  

class Connection:
    def __init__(self):
        self.conn = self.connect_db()
        self.cursor = self.conn.cursor()

    def connect_db(self):
        try:
            conn = psycopg2.connect(
                host=config.DB_HOST,
                database=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                sslmode='require'  # Enforce SSL for connection
            )
            print("DB_CONNECTOR: Successfully connected to the database.")
            return conn
        except Exception as e:
            print("DB_CONNECTOR: Failed to connect database.")
            print("Error: ")
            print(e)

    def close_connection(self):
        print("DB_CONNECTOR: Successfully closed connection.")
        self.conn.close()

        