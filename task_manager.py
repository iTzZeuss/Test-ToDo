import database_connector

class TaskManager:
    def __init__(self, connector:database_connector.Connection):
        self.conn = connector.conn
        self.c = connector.cursor

        # Create tasks table if it doesn't exis
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                header TEXT NOT NULL,
                description TEXT,
                photopath TEXT,
                state BOOLEAN NOT NULL DEFAULT FALSE
            )
        ''')

        self.conn.commit()
        print("TASK_MANAGER: Alive!")

    # Function to search tasks based on user query
    def search_tasks(self, query):
        # Use ILIKE for case-insensitive search in both header and description fields
        search_query = f"%{query}%"  # Surround query with wildcards for partial matching
        self.c.execute('''
            SELECT * FROM tasks
            WHERE header ILIKE %s OR description ILIKE %s
        ''', (search_query, search_query))

        # Fetch all matching tasks
        tasks = self.c.fetchall()
        
        # If there are matching tasks, format them into a list of dictionaries
        print(f"TASK_MANAGER: Search for '{query}' completed successfully.")
        if tasks:
            tasklist = []
            for task in tasks:
                tasklist.append({
                    "id": task[0],
                    "header": task[1],
                    "description": task[2],
                    "photo_path": task[3],
                    "status": task[4]
                })
            return tasklist
        else:
            return []  # Return an empty list if no matches found

    # Function to add a new task
    def add_task(self, header, description, photopath, state=False):
        self.c.execute('''
            INSERT INTO tasks (header, description, photopath, state)
            VALUES (%s, %s, %s, %s)
        ''', (header, description, photopath, state))
        self.conn.commit()

        print("TASK_MANAGER: Task added successfully.")

    # Function to update an existing task by id
    def update_task(self, task_id, header=None, description=None, photopath=None, state=None):
        task = self.get_task(task_id)
        if task:
            self.c.execute('''
                UPDATE tasks SET
                header = COALESCE(%s, header),
                description = COALESCE(%s, description),
                photopath = COALESCE(%s, photopath),
                state = COALESCE(%s, state)
                WHERE id = %s
            ''', (header, description, photopath, state, task_id))
            self.conn.commit()
            print(f"TASK_MANAGER: Task {task_id} updated successfully!")
        else:
            print("TASK_MANAGER: Task not found! update_task() function.")

    # Function to delete a task by id
    def delete_task(self, task_id):
        self.c.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
        self.conn.commit()
        print(f"TASK_MANAGER: Task {task_id} deleted successfully!")

    # Function to mark a task as done
    def mark_task_done(self, task_id):
        self.update_task(self, task_id, state=True)
        print(f"TASK_MANAGER: Task {task_id} successfully marked as done.")

    def mark_task_notdone(self, task_id):
        self.update_task(task_id, state=False)
        print(f"TASK_MANAGER: Task {task_id} successfully marked as not done.")

    # Function to retrieve a task by id
    def get_task(self, task_id):
        self.c.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
        info = self.c.fetchone()
        print(f"TASK_MANAGER: Fetched single task with id {task_id} successfully.")
        return {
            "id" : info[0],
            "header" : info[1],
            "description" : info[2],
            "photo_path" : info[3],
            "status" : info[4]
        }
    

    # Function to list all tasks
    def list_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        tasks = self.c.fetchall()
        tasklist = []
        for task in tasks:
            tasklist.append({
                "id": task[0], 
                "header": task[1], 
                "description": task[2], 
                "photo_path": task[3], 
                "status": task[4]
            })
        print("TASK_MANAGER: Fetched whole task list successfully.")
        return tasklist
    
