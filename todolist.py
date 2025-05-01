

import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = 'tasks.json'

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = load_tasks()

        self.task_var = tk.StringVar()

        self.create_widgets()
        self.load_task_list()

    def create_widgets(self):
        tk.Label(self.root, text="Task:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.task_var, width=40).pack(pady=5)
        tk.Button(self.root, text="Add Task", command=self.add_task).pack(pady=5)

        self.listbox = tk.Listbox(self.root, width=50, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        tk.Button(self.root, text="Mark Completed", command=self.mark_completed).pack(pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).pack(pady=5)

    def load_task_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else "✗"
            self.listbox.insert(tk.END, f"[{status}] {task['description']}")

    def add_task(self):
        description = self.task_var.get().strip()
        if description:
            self.tasks.append({"description": description, "completed": False})
            self.task_var.set("")
            self.save_and_reload()
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")

    def mark_completed(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['completed'] = True
            self.save_and_reload()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.save_and_reload()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def save_and_reload(self):
        save_tasks(self.tasks)
        self.load_task_list()

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
