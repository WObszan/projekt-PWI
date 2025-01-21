import threading
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
from filtry_sortowanie import FiltrySortowanie
from powiadomienia import SendingReminder
from statystyki import TaskStats
from categories_tags import CategoryTagManager
import json
import matplotlib.pyplot as plt  # Importujemy matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
# File path for tasks
TASKS_FILE = "tasks.json"
DEFAULT_EMAIL = "common.email@example.com"

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

        # Load tasks into the GUI on startup
        self.refresh_task_list()

    def setup_gui(self):
        # Frame for buttons
        button_frame = tk.Frame(self.root, padx=10, pady=10)
        button_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Buttons for actions
        tk.Button(button_frame, text="Set Default Email", command=self.set_default_email, width=20).pack(pady=5)
        tk.Button(button_frame, text="Add Task", command=self.add_task_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Remove Task", command=self.remove_task_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Filter Tasks by Key", command=self.filter_tasks_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Filter Tasks by Date", command=self.filter_tasks_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Sort Tasks", command=self.sort_tasks_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Task Statistics", command=self.view_statistics, width=20).pack(pady=5)
        tk.Button(button_frame, text="Manage Categories", command=self.manage_categories_window, width=20).pack(pady=5)
        tk.Button(button_frame, text="Exit", command=self.root.quit, width=20).pack(pady=5)

        # Frame for task list display
        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.task_tree = ttk.Treeview(self.display_frame, columns=("ID", "Description", "Priority", "Deadline", "Time", "Status", "Category"), show="headings")
        for col in self.task_tree["columns"]:
            self.task_tree.heading(col, text=col)
            self.task_tree.column(col, width=100)
        self.task_tree.pack(expand=True, fill=tk.BOTH)

        # Bind the task click event to mark it as completed
        self.task_tree.bind("<ButtonRelease-1>", self.on_task_click)

    def on_task_click(self, event):
        # Get the item that was clicked
        item_id = self.task_tree.selection()
        if item_id:
            task_id = self.task_tree.item(item_id[0], "values")[0]  # Get task ID from clicked item
            self.mark_task_completed(int(task_id))

    def mark_task_completed(self, task_id):
        # Find the task by its ID and change its status to "completed"
        task_found = False
        for task in self.filtry_sortowanie.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task_found = True
                break

        if task_found:
            # Save updated tasks to file
            with open(TASKS_FILE, 'w', encoding='utf-8') as file:
                json.dump({"zadania": self.filtry_sortowanie.tasks}, file, ensure_ascii=False, indent=4)
            # Refresh the task list in the UI
            self.refresh_task_list()
            messagebox.showinfo("Success", f"Task {task_id} marked as completed.")
        else:
            messagebox.showerror("Error", f"Task with ID {task_id} not found.")



    def load_categories(self):
            """
            Load available categories from the tasks JSON file.
            """
            try:
                with open(TASKS_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    # Extract unique categories from the tasks
                    return list({task["kategoria"] for task in data.get("zadania", [])})
            except (FileNotFoundError, json.JSONDecodeError):
                # If the file doesn't exist or is invalid, return an empty list
                return []

    def add_task_window(self):
        # Create a new window for adding tasks
        window = tk.Toplevel(self.root)
        window.title("Add Task")
        window.geometry("400x400")

        # Labels and entries for task attributes
        tk.Label(window, text="Description:").pack(pady=4)
        description_entry = tk.Entry(window)
        description_entry.pack(pady=4)

        tk.Label(window, text="Priority:").pack(pady=4)
        priority_options = ["wysoki", "średni", "niski"]
        priority_combobox = ttk.Combobox(window, values=priority_options, state="readonly")
        priority_combobox.set("średni")  # Set default value
        priority_combobox.pack(pady=4)

        tk.Label(window, text="Deadline (choose date):").pack(pady=4)
        # Use DateEntry for selecting a date
        deadline_entry = DateEntry(window, date_pattern="yyyy-MM-dd", width=12, background="black",
                                   foreground="white", borderwidth=2)
        deadline_entry.pack(pady=4)

        tk.Label(window, text="Time (HH:MM):").pack(pady=5)

        # Create a Frame to place hour and minute controls on the same row
        time_frame = tk.Frame(window)
        time_frame.pack(pady=4)

        # Hour Spinbox (0 to 23)
        hour_spinbox = tk.Spinbox(time_frame, from_=0, to=23, width=5)
        hour_spinbox.pack(side="left", padx=5)
        hour_spinbox.delete(0, 'end')  # Usuwamy domyślną wartość
        hour_spinbox.insert(0, '12')  # Wstawiamy wartość '12'

        # Minute Spinbox (0 to 59)
        minute_spinbox = tk.Spinbox(time_frame, from_=0, to=59, width=5)
        minute_spinbox.pack(side="left", padx=5)
        minute_spinbox.delete(0, 'end')  # Usuwamy domyślną wartość
        minute_spinbox.insert(0, '12')


        tk.Label(window, text="Category:").pack(pady=4)
        categories = self.load_categories()
        category_combobox = ttk.Combobox(window, values=categories, state="normal")
        category_combobox.pack(pady=4)



        def save_task():
            try:
                id = max((task["id"] for task in self.filtry_sortowanie.tasks), default=0) + 1
                description = description_entry.get()
                priority = priority_combobox.get()
                deadline = deadline_entry.get()
                hour = hour_spinbox.get()
                minute = minute_spinbox.get()
                time = f"{int(hour):02}:{int(minute):02}"
                category = category_combobox.get()
                status = "not completed"

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
                    "email": DEFAULT_EMAIL,  # Use the default email
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

        tk.Button(window, text="Save Task", command=save_task, width=10, height=1, font=("Helvetica", 10)).pack(pady=20)

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


    def view_statistics(self):
        # Sprawdzamy, czy wykres jest już widoczny i ukrywamy go jeśli tak
        if hasattr(self, 'chart_canvas') and self.chart_canvas.get_tk_widget().winfo_ismapped():
            self.chart_canvas.get_tk_widget().pack_forget()

        # Tworzymy nowe okno wyboru statystyki
        stat_window = tk.Toplevel(self.root)
        stat_window.title("Select Statistic Type")
        stat_window.geometry("300x200")

        # Opis dostępnych statystyk
        tk.Label(stat_window, text="Select the statistics to display:").pack(pady=10)

        # Lista dostępnych opcji statystyk
        options = ["Status", "Category", "Deadline"]
        stat_choice = tk.StringVar(stat_window)
        stat_choice.set(options[0])  # Domyślnie wybrana opcja

        # Tworzymy rozwijane menu z opcjami
        option_menu = tk.OptionMenu(stat_window, stat_choice, *options)
        option_menu.pack(pady=10)

        # Funkcja do generowania wykresu na podstawie wybranej opcji
        def show_chart():
            selected_stat = stat_choice.get()
            if selected_stat == "Status":
                self.plot_status_statistics()  # Rysowanie wykresu dla statusu
            elif selected_stat == "Category":
                self.plot_category_statistics()  # Rysowanie wykresu dla kategorii
            elif selected_stat == "Deadline":
                self.plot_deadline_statistics()  # Rysowanie wykresu dla deadline
            stat_window.destroy()  # Zamykamy okno wyboru po narysowaniu wykresu

        # Przycisk do zatwierdzenia wyboru
        tk.Button(stat_window, text="Show Statistics", command=show_chart).pack(pady=20)

    def plot_status_statistics(self):
        # Wykres dla statusu (wykorzystanie istniejącej funkcji)
        status_data = self.stats.c_by_status()
        status_labels = list(status_data.keys())
        status_counts = list(status_data.values())
        colors = ['green' if status == 'completed' else 'red' for status in status_labels]

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(status_labels, status_counts, color=colors)
        ax.set_title('Task Statuses')
        ax.set_xlabel('Status')
        ax.set_ylabel('Count')

        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack()

    def filter_tasks_window(self):
        # Implement filtering functionality here
        pass

    def filter_tasks_date_window(self):
        # Implement filtering functionality here
        pass

    def sort_tasks_window(self):
        window = tk.Toplevel(self.root)
        window.title("Sort Tasks")
        window.geometry("300x200")

        tk.Label(window, text="Select sorting key:").pack(pady=5)
        key_mapping = {
            "ID": "id",
            "Description": "opis",
            "Priority": "priorytet",
            "Deadline": "termin",
            "Time": "godzina",
            "Status": "status",
            "Category": "kategoria"
        }
        key_var = tk.StringVar(value="ID")
        key_menu = tk.OptionMenu(window, key_var, *key_mapping.keys())
        key_menu.pack(pady=5)

        tk.Label(window, text="Select sorting order:").pack(pady=5)
        order_var = tk.StringVar(value="ascending")
        ascending_radio = tk.Radiobutton(window, text="Ascending", variable=order_var, value="ascending")
        ascending_radio.pack()
        descending_radio = tk.Radiobutton(window, text="Descending", variable=order_var, value="descending")
        descending_radio.pack()

        def apply_sorting():
            key = key_mapping[key_var.get()]
            order = order_var.get()
            try:
                reverse = True if order == "descending" else False
                self.filtry_sortowanie.tasks = self.filtry_sortowanie.sort_tasks(key, reverse)
                with open(TASKS_FILE, 'w', encoding='utf-8') as file:
                    json.dump({"zadania": self.filtry_sortowanie.tasks}, file, ensure_ascii=False, indent=4)
                self.refresh_task_list()
                window.destroy()
                messagebox.showinfo("Success", "Tasks sorted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to sort tasks: {e}")

        tk.Button(window, text="Sort", command=apply_sorting).pack(pady=20)

    def plot_category_statistics(self):
        # Wykres dla kategorii
        categories_data = self.stats.c_by_categories()
        category_labels = list(categories_data.keys())
        category_counts = list(categories_data.values())

        fig, ax = plt.subplots(figsize=(10, 8))
        ax.bar(category_labels, category_counts, color='blue')

        # Dodaj set_xticks przed set_xticklabels
        ax.set_xticks(range(len(category_labels)))
        ax.set_xticklabels(category_labels, rotation=90)

        ax.set_title('Task Categories')
        ax.set_xlabel('Category')
        ax.set_ylabel('Count')

        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack()

    def plot_deadline_statistics(self):
        # Wykres dla deadline (ile zadań do zrobienia dzisiaj, jutro, w tym tygodniu)
        deadline_data = self.stats.close_to_deadline()
        deadline_labels = list(deadline_data.keys())
        deadline_counts = list(deadline_data.values())

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(deadline_labels, deadline_counts, color='purple')
        ax.set_title('Tasks Close to Deadline')
        ax.set_xlabel('Deadline')
        ax.set_ylabel('Count')

        self.chart_canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.chart_canvas.draw()
        self.chart_canvas.get_tk_widget().pack()

    def manage_categories_window(self):
        # Implement category management functionality here
        pass

    def refresh_task_list(self):
        # Czyszczenie obecnych wpisów w widoku drzewa
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)

        # Dodawanie tylko zadań, które nie są ukończone
        for task in self.filtry_sortowanie.tasks:
            if task["status"] != "completed":
                self.task_tree.insert("", tk.END, values=(
                    task["id"], task["opis"], task["priorytet"], task["termin"], task["godzina"], task["status"],
                    task["kategoria"]
                ))

    def set_default_email(self):
        # Prompt the user to input a new default email
        new_email = simpledialog.askstring("Set Default Email", "Enter the default email address:")
        if new_email:
            global DEFAULT_EMAIL
            DEFAULT_EMAIL = new_email
            messagebox.showinfo("Success", f"Default email set to: {DEFAULT_EMAIL}")



# Main function
def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
