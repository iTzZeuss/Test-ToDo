import sqlite3
import config

# Connect to or create a database
conn = sqlite3.connect(config.DB_PATH)
c = conn.cursor()

# Create tasks table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        header TEXT NOT NULL,
        description TEXT,
        photopath TEXT,
        state BOOLEAN NOT NULL CHECK (state IN (0, 1))
    )
''')

conn.commit()

# Function to add a new task
def add_task(header, description, photopath, state=False):
    c.execute('''
        INSERT INTO tasks (header, description, photopath, state)
        VALUES (?, ?, ?, ?)
    ''', (header, description, photopath, state))
    conn.commit()
    print("Task added successfully!")

# Function to update an existing task by id
def update_task(task_id, header=None, description=None, photopath=None, state=None):
    task = get_task(task_id)
    if task:
        c.execute('''
            UPDATE tasks SET
            header = COALESCE(?, header),
            description = COALESCE(?, description),
            photopath = COALESCE(?, photopath),
            state = COALESCE(?, state)
            WHERE id = ?
        ''', (header, description, photopath, state, task_id))
        conn.commit()
        print(f"Task {task_id} updated successfully!")
    else:
        print("Task not found!")

# Function to delete a task by id
def delete_task(task_id):
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    print(f"Task {task_id} deleted successfully!")

# Function to mark a task as done
def mark_task_done(task_id):
    update_task(task_id, state=True)

# Function to retrieve a task by id
def get_task(task_id):
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    return c.fetchone()

# Function to list all tasks
def list_tasks():
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    for task in tasks:
        done_status = 'Done' if task[4] else 'Not Done'
        print(f"ID: {task[0]}, Header: {task[1]}, Description: {task[2]}, Photo: {task[3]}, Status: {done_status}")

# Close the connection (You can do this when done with all operations)
def close_connection():
    conn.close()




# Example usage
if __name__ == '__main__':
    # Add a new task
    add_task('Buy groceries', 'Buy milk, bread, and eggs', '/path/to/photo.jpg')
    
    # List all tasks
    print("\nTasks List:")
    list_tasks()

    # Update task with id 1
    update_task(1, description="Buy milk, bread, eggs, and cheese")

    # Mark task 1 as done
    mark_task_done(1)

    # List tasks after update
    print("\nTasks after update:")
    list_tasks()

    # Delete task with id 1
    delete_task(1)

    # List tasks after deletion
    print("\nTasks after deletion:")
    list_tasks()

    # Close connection
    close_connection()
