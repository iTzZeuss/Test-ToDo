import database_connector

class AccountManager:
    def __init__(self, connector:database_connector.Connection):
        self.conn = connector.conn
        self.c = connector.cursor

        # Create tasks table if it doesn't exis
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                serial SERIAL PRIMARY KEY,
                user_name TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')

        self.conn.commit()
        print("ACCOUNT_MANAGER: Alive!")
    
    def create_new_account():
        return
    
    def edit_account():
        return
    
    def delete_account():
        return
    
    def get_account_list():
        return
    
    def get_account_info():
        return #by id
    