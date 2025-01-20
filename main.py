import threading
from datetime import datetime
from filtry_sortowanie import FiltrySortowanie
from powiadomienia import SendingReminder
from statystyki import TaskStats
from categories_tags import CategoryTagManager
import json

# File path for tasks
TASKS_FILE = "tasks.json"

# Main application
def main():
    # Initialize necessary classes
    filtry_sortowanie = FiltrySortowanie(TASKS_FILE)
    reminder = SendingReminder(TASKS_FILE)
    stats = TaskStats(TASKS_FILE)
    category_manager = CategoryTagManager(TASKS_FILE)

    # Start the reminder system in a separate thread
    reminder_thread = threading.Thread(target=reminder.run_in_background, args=(TASKS_FILE,), daemon=True)
    reminder_thread.start()

    # Main menu loop
    while True:
        print("\n=== Task Management Application ===")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. View All Tasks")
        print("4. Filter Tasks by Date")
        print("5. Sort Tasks by Priority or Deadline")
        print("6. View Task Statistics")
        print("7. Manage Categories")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            # Add a task
            id = len(filtry_sortowanie.tasks) + 1
            opis = input("Enter task description: ")
            priorytet = input("Enter priority (wysoki, średni, niski): ")
            termin = input("Enter deadline (YYYY-MM-DD): ")
            godzina = input("Enter time (HH:MM): ")
            email = input("Enter email for reminders: ")
            status = "nie zrobione"
            kategoria = input("Enter category: ")

            new_task = {
                "id": id,
                "opis": opis,
                "priorytet": priorytet,
                "termin": termin,
                "godzina": godzina,
                "email": email,
                "status": status,
                "kategoria": kategoria
            }
            filtry_sortowanie.tasks.append(new_task)
            with open(TASKS_FILE, 'w', encoding='utf-8') as file:
                json.dump({"zadania": filtry_sortowanie.tasks}, file, ensure_ascii=False, indent=4)
            print("Task added successfully!")
            category_manager = CategoryTagManager(TASKS_FILE)

        elif choice == "2":
            # Remove a task
            task_id = int(input("Enter the task ID to remove: "))
            filtry_sortowanie.tasks = [task for task in filtry_sortowanie.tasks if task["id"] != task_id]
            with open(TASKS_FILE, 'w', encoding='utf-8') as file:
                json.dump({"zadania": filtry_sortowanie.tasks}, file, ensure_ascii=False, indent=4)
            print("Task removed successfully!")

        elif choice == "3":
            # View all tasks
            for task in filtry_sortowanie.tasks:
                print(task)

        elif choice == "4":
            # Filter tasks by date range
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            filtered_tasks = filtry_sortowanie.filter_tasks_by_date(start_date, end_date)
            for task in filtered_tasks:
                print(task)

        elif choice == "5":
            # Sort tasks
            key = input("Enter key to sort by (termin, priorytet): ")
            reverse = input("Sort in descending order? (yes/no): ").lower() == "yes"
            sorted_tasks = filtry_sortowanie.sort_tasks(key, reverse)
            for task in sorted_tasks:
                print(task)

        elif choice == "6":
            # View task statistics
            print("Task Count by Status:")
            print(stats.c_by_status())
            print("\nTask Count by Category:")
            print(stats.c_by_categories())
            print("\nTasks Close to Deadline:")
            print(stats.close_to_deadline())

        elif choice == "7":
            # Manage categories
            print("\n1. Add Category")
            print("2. View All Categories")
            category_choice = input("Choose an option: ")

            if category_choice == "1":
                category_name = input("Enter category name: ")
                category_manager.add_category(category_name)
                print(f"Category '{category_name}' added!")
            elif category_choice == "2":
                print("Categories:")
                for category in category_manager.categories:
                    print(f"- {category}")

        elif choice == "8":
            # Exit the program
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
