import database_connector
from werkzeug.security import generate_password_hash, check_password_hash

#TODO: make some refactoring

class AccountManager:
    def __init__(self, connector:database_connector.Connection):
        self.conn = connector.conn
        self.c = connector.cursor

        # Create users table if it doesn't exist
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user'  -- 'user' or 'admin'
            )
        ''')

        self.conn.commit()

    def check_username_exists(self, username):
        self.c.execute('SELECT 1 FROM users WHERE username = %s', (username,))
        return self.c.fetchone() is not None  # Returns True if username exists, else False

    def register_user(self, username, password, role='user'):
        if self.check_username_exists(username):
            print("Username already exists!")
            return
        password_hash = generate_password_hash(password)  # Hash the password for security TODO: implement own hashing system
        self.c.execute('''
            INSERT INTO users (username, password_hash, role)
            VALUES (%s, %s, %s)
        ''', (username, password_hash, role))
        self.conn.commit()
        print("User registered successfully!")

    def check_login_info(self, username, password):
        self.c.execute('''
            SELECT * FROM users WHERE username = %s
        ''', (username,))
        user = self.c.fetchone()
        if user:
            if check_password_hash(user[2], password):  # Compare stored hash with input password #TODO: own security system
                return {
                    "id": user[0],
                    "username": user[1],
                    "role": user[3]
                }
            else:
                return None  # Password mismatch
        else:
            return None  # User not found
        
    def update_password(self, user_id, old_password, new_password):
        user = self.get_user(user_id)
        if user and check_password_hash(user['password_hash'], old_password):  # Verify old password
            new_password_hash = generate_password_hash(new_password)
            self.c.execute('''
                UPDATE users SET password_hash = %s WHERE id = %s
            ''', (new_password_hash, user_id))
            self.conn.commit()
            print("Password updated successfully!")
        else:
            print("Old password is incorrect or user not found.")

    def delete_user(self, user_id):
        self.c.execute('DELETE FROM users WHERE id = %s', (user_id,))
        self.conn.commit()
        print(f"User {user_id} deleted successfully!")

    def get_user(self, user_id):
        self.c.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        info = self.c.fetchone()
        if info:
            return {
                "id": info[0],
                "username": info[1],
                "password_hash": info[2],
                "role": info[3]
            }
        else:
            return None

    def list_users(self):
        self.c.execute('SELECT * FROM users')
        users = self.c.fetchall()
        userlist = []
        for user in users:
            userlist.append({
                "id": user[0],
                "username": user[1],
                "role": user[3]
            })
        return userlist

