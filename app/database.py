import sqlite3
import os
from app.logger import logger


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

DB = os.path.join(DATA_DIR, "assistant.db")

class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB , check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,name TEXT)"
        )

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY AUTOINCREMENT,note TEXT NOT NULL)"
        )

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,task TEXT NOT NULL,completed INTEGER DEFAULT 0)"
        )

        self.conn.commit()
        
    def set_name(self, name):
        self.cursor.execute(
            "SELECT * FROM user WHERE id = 1"
        )

        row = self.cursor.fetchone()

        if row:
            self.cursor.execute(
                "UPDATE user SET name = ? WHERE id = 1",
                (name,)
            )
        else:
            self.cursor.execute(
                "INSERT INTO user (id, name) VALUES (1, ?)",
                (name,)
            )

        self.conn.commit()
        logger(f"Set Name - {name}")

    def get_name(self):
        self.cursor.execute(
            "SELECT name FROM user"
        )
        row = self.cursor.fetchone()
        if row:
            return row[0]
        return ""

    def add_note(self, note):
        self.cursor.execute(
            "INSERT INTO notes(note) VALUES (?)",
            (note,))
        self.conn.commit()
        logger(f"Added Note - {note}")

    def get_notes(self):
        self.cursor.execute(
            "SELECT * FROM notes"
        )
        notes = self.cursor.fetchall()
        return notes
    
    def get_note_by_id(self, note_id):
        self.cursor.execute(
            "SELECT note FROM notes WHERE id = ?",
            (note_id,)
        )
        row = self.cursor.fetchone()

        if row:
            return row[0]
        return None

    def delete_note(self, note_id):
        self.cursor.execute(
            "DELETE FROM notes WHERE id = ?",
            (note_id,)
        )

        self.conn.commit()

        logger("Deleted Note")

        if self.cursor.rowcount == 0:
            return False

        return True
    def update_note(self , note_id , new_note):
        self.cursor.execute(
            "UPDATE notes SET note=(?) WHERE id = (?)",
             (new_note,note_id)
        )
        self.conn.commit()
        logger(f"Updated Note - {new_note}")
    def update_task(self , task_id , new_task):
        self.cursor.execute(
            "UPDATE tasks SET task=(?) WHERE id = (?)",
             (new_task,task_id)
        )
        self.conn.commit()
        logger(f"Updated Note - {new_task}")
        
    def add_task(self, task):
        self.cursor.execute(
            "INSERT INTO tasks (task) VALUES (?)",
            (task,))
        self.conn.commit()
        logger(f"Added Task - {task}")
        
    def get_tasks(self):
        self.cursor.execute(
            "SELECT * FROM tasks"
        )
        tasks = self.cursor.fetchall()
        return tasks
        
    def complete_task(self, task_id):
        self.cursor.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?",
            (task_id,)
        )
        self.conn.commit()
        logger("Task Completed")
        if self.cursor.rowcount == 0:
            return False

        return True
    def get_task_by_id(self,task_id):
        self.cursor.execute(
            "SELECT task FROM tasks WHERE id = ?",
            (task_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return row[0]
        return None
        
    def delete_task(self, task_id):
        self.cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        self.conn.commit()
        logger("Deleted Task")
        if self.cursor.rowcount == 0:
            return False
        return True

    def get_task_stats(self):
        self.cursor.execute(
                "SELECT COUNT(*) FROM tasks",
                )
        total = self.cursor.fetchone()[0]
        self.cursor.execute(
                "SELECT COUNT(*) FROM tasks WHERE completed = 1",
                )
        completed = self.cursor.fetchone()[0]
        pending = total-completed
        logger("Viewed Task Stats")
        output = (
            f"===== TASK STATS =====\n"
            f"Total Tasks: {total}\n"
            f"Completed Tasks: {completed}\n"
            f"Pending Tasks: {pending}"
        )
        return output
    
    def history_viewer(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        LOG_FILE = os.path.join(BASE_DIR, "data", "History.txt")
        try:
            with open(LOG_FILE, "r") as f:
                logger("Viewed History")
                return f.read().strip()
        except FileNotFoundError:
            return "No history found."
    def close(self):
        self.conn.close()