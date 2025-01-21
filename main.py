import threading
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from filtry_sortowanie import FiltrySortowanie
from powiadomienia import SendingReminder
from statystyki import TaskStats
from categories_tags import CategoryTagManager
import json

# File path for tasks
TASKS_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Management Application")
        self.root.geometry("1200x600")
        
        # Initialize necessary classes
        self.filtry_sortowanie = FiltrySortowanie(TASKS_FILE)
        self.reminder = SendingReminder(TASKS_FILE)
        self.stats = TaskStats(TASKS_FILE)
        self.category_manager = CategoryTagManager(TASKS_FILE)
        
        # Start the reminder system in a separate thread
        reminder_thread = threading.Thread(target=self.reminder.run_in_background, args=(TASKS_FILE,), daemon=True)
        reminder_thread.start()

        # Setup GUI
        self.setup_gui()

    def setup_gui(self):
        # Frame for buttons
        button_frame = tk.Frame(self.root, padx=10, pady=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Buttons for actions
        tk.Button(button_frame, text="Add Task", command=self.add_task_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Remove Task", command=self.remove_task_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="View All Tasks", command=self.view_all_tasks, width=20).pack(pady=5)
        tk.Button(button_frame, text="Filter Tasks by Date", command=self.filter_tasks_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Sort Tasks", command=self.sort_tasks_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Task Statistics", command=self.view_statistics, width=20).pack(pady=5)
        tk.Button(button_frame, text="Manage Categories", command=self.manage_categories_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Exit", command=self.root.quit, width=20).pack(pady=5)

        # Frame for task list display
        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.task_tree = ttk.Treeview(self.display_frame, columns=("ID", "Description", "Priority", "Deadline", "Time", "Email", "Status", "Category"), show="headings")
        for col in self.task_tree["columns"]:
            self.task_tree.heading(col, text=col)
            self.task_tree.column(col, width=100)
        self.task_tree.pack(expand=True, fill=tk.BOTH)

    def add_task_window(self):
        # Create a new window for adding tasks
        window = tk.Toplevel(self.root)
        window.title("Add Task")
        window.geometry("400x400")

        # Labels and entries for task attributes
        tk.Label(window, text="Description:").pack(pady=5)
        description_entry = tk.Entry(window)
        description_entry.pack(pady=5)

        tk.Label(window, text="Priority (wysoki, średni, niski):").pack(pady=5)
        priority_entry = tk.Entry(window)
        priority_entry.pack(pady=5)

        tk.Label(window, text="Deadline (YYYY-MM-DD):").pack(pady=5)
        deadline_entry = tk.Entry(window)
        deadline_entry.pack(pady=5)

        tk.Label(window, text="Time (HH:MM):").pack(pady=5)
        time_entry = tk.Entry(window)
        time_entry.pack(pady=5)

        tk.Label(window, text="Email for reminders:").pack(pady=5)
        email_entry = tk.Entry(window)
        email_entry.pack(pady=5)

        tk.Label(window, text="Category:").pack(pady=5)
        category_entry = tk.Entry(window)
        category_entry.pack(pady=5)

        def save_task():
            try:
                id = max((task["id"] for task in self.filtry_sortowanie.tasks), default=0) + 1
                description = description_entry.get()
                priority = priority_entry.get().lower()
                deadline = deadline_entry.get()
                time = time_entry.get()
                email = email_entry.get()
                category = category_entry.get()
                status = "nie zrobione"

                # Validate inputs
                datetime.strptime(deadline, "%Y-%m-%d")  # Validate date
                datetime.strptime(time, "%H:%M")  # Validate time

                if priority not in {"wysoki", "średni", "niski"}:
                    raise ValueError("Invalid priority value!")

                # Add task
                new_task = {
                    "id": id,
                    "opis": description,
                    "priorytet": priority,
                    "termin": deadline,
                    "godzina": time,
                    "email": email,
                    "status": status,
                    "kategoria": category
                }
                self.filtry_sortowanie.tasks.append(new_task)
                with open(TASKS_FILE, 'w', encoding='utf-8') as file:
                    json.dump({"zadania": self.filtry_sortowanie.tasks}, file, ensure_ascii=False, indent=4)
                self.category_manager.add_category(category)

                # Refresh task list
                self.refresh_task_list()
                window.destroy()
                messagebox.showinfo("Success", "Task added successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add task: {e}")

        tk.Button(window, text="Save Task", command=save_task).pack(pady=20)

    def remove_task_window(self):
        window = tk.Toplevel(self.root)
        window.title("Remove Task")
        window.geometry("300x200")

        tk.Label(window, text="Enter Task ID to Remove:").pack(pady=5)
        task_id_entry = tk.Entry(window)
        task_id_entry.pack(pady=5)

        def remove_task():
            try:
                task_id = int(task_id_entry.get())
                self.filtry_sortowanie.tasks = [task for task in self.filtry_sortowanie.tasks if task["id"] != task_id]
                with open(TASKS_FILE, 'w', encoding='utf-8') as file:
                    json.dump({"zadania": self.filtry_sortowanie.tasks}, file, ensure_ascii=False, indent=4)
                self.refresh_task_list()
                window.destroy()
                messagebox.showinfo("Success", "Task removed successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid Task ID!")

        tk.Button(window, text="Remove Task", command=remove_task).pack(pady=20)

    def view_all_tasks(self):
        self.refresh_task_list()

    def filter_tasks_window(self):
        # Implement filtering functionality here
        pass

    def sort_tasks_window(self):
        # Implement sorting functionality here
        pass

    def view_statistics(self):
        # Implement statistics functionality here
        pass

    def manage_categories_window(self):
        # Implement category management functionality here
        pass

    def refresh_task_list(self):
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        for task in self.filtry_sortowanie.tasks:
            self.task_tree.insert("", tk.END, values=(
                task["id"], task["opis"], task["priorytet"], task["termin"], task["godzina"], task["email"], task["status"], task["kategoria"]
            ))

# Main function
def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
