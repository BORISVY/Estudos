from datetime import datetime
from app.data.db import get_connection
from app.models.task import Task

class TaskManager():
    def get_all_tasks(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        conn.close()
        tasks = []

        for row in rows:
            tasks.append({
                "id": row[0],
                "title": row[1],
                "desc": row[2],
                "status": row[3],
                "created_at": row[4]
            })
        return tasks
    
    def get_task_by_id(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return {
                "id": row[0],
                "title": row[1],
                "desc": row[2],
                "status": row[3],
                "created_at": row[4]
            }
        return None

    def create_task(self, title, desc):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO tasks (title, desc) VALUES (?, ?)", (title, desc))
        conn.commit()
        conn.close()

    def delete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

        affected = cursor.rowcount
        conn.close()

        return affected > 0
    
    def complete_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE tasks SET status = '1' WHERE id = ?", (task_id,))
        conn.commit()

        affected = cursor.rowcount
        conn.close()

        return affected > 0
    
    def reopen_task(self, task_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE tasks SET status = '0' WHERE id = ?", (task_id,))
        conn.commit()

        affected = cursor.rowcount
        conn.close()

        return affected > 0
    
    def search_tasks(self, title):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tasks WHERE title LIKE ? ", (f"%{title}%",))
        rows = cursor.fetchall()

        conn.close()

        return [{
            "id": row[0],
            "title": row[1],
            "desc": row[2],
            "status": bool(row[3]),
            "created_at": row[4]
        } for row in rows]