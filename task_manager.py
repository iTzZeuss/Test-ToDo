import psycopg2
import config  # This should contain your PostgreSQL connection settings (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

# Connect to the PostgreSQL database
def connect_db():
    conn = psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        sslmode='require'  # Enforce SSL for connection
    )
    return conn

conn = connect_db()
c = conn.cursor()

# Create tasks table if it doesn't exis
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        header TEXT NOT NULL,
        description TEXT,
        photopath TEXT,
        state BOOLEAN NOT NULL DEFAULT FALSE
    )
''')

conn.commit()

# Function to add a new task
def add_task(header, description, photopath, state=False):
    c.execute('''
        INSERT INTO tasks (header, description, photopath, state)
        VALUES (%s, %s, %s, %s)
    ''', (header, description, photopath, state))
    conn.commit()
    print("Task added successfully!")

# Function to update an existing task by id
def update_task(task_id, header=None, description=None, photopath=None, state=None):
    task = get_task(task_id)
    if task:
        c.execute('''
            UPDATE tasks SET
            header = COALESCE(%s, header),
            description = COALESCE(%s, description),
            photopath = COALESCE(%s, photopath),
            state = COALESCE(%s, state)
            WHERE id = %s
        ''', (header, description, photopath, state, task_id))
        conn.commit()
        print(f"Task {task_id} updated successfully!")
    else:
        print("Task not found!")

# Function to delete a task by id
def delete_task(task_id):
    c.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    print(f"Task {task_id} deleted successfully!")

# Function to mark a task as done
def mark_task_done(task_id):
    update_task(task_id, state=True)

def mark_task_notdone(task_id):
    update_task(task_id, state=False)

# Function to retrieve a task by id
def get_task(task_id):
    c.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    info = c.fetchone()
    return {
        "id" : info[0],
        "header" : info[1],
        "description" : info[2],
        "photo_path" : info[3],
        "status" : info[4]
    }

# Function to list all tasks
def list_tasks():
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
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

# Close the connection (You can do this when done with all operations)
def close_connection():
    conn.close()