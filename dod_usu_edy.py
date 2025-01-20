import json
import os

# Plik JSON do przechowywania danych
TASKS_FILE = "tasks.json"

# Funkcja do wczytywania danych z pliku JSON
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

# Funkcja do zapisywania danych do pliku JSON
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Dodawanie nowego zadania
def add_task(tasks, opis, priorytet, termin, godzina, email):
    new_id = max([task['id'] for task in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "opis": opis,
        "priorytet": priorytet,
        "termin": termin,
        "godzina": godzina,
        "email": email
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Dodano zadanie: {new_task}")

# Edycja istniejącego zadania
def edit_task(tasks, task_id, **kwargs):
    for task in tasks:
        if task["id"] == task_id:
            for key, value in kwargs.items():
                if key in task:
                    task[key] = value
            save_tasks(tasks)
            print(f"Zadanie o ID {task_id} zostało zmienione.")
            return
    print(f"Nie znaleziono zadania o ID {task_id}.")

# Usuwanie zadania
def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            # Aktualizacja ID zadań
            for i, task in enumerate(tasks):
                task["id"] = i + 1
            save_tasks(tasks)
            print(f"Usunięto zadanie o ID {task_id}. Zaktualizowano ID pozostałych zadań.")
            return
    print(f"Nie znaleziono zadania o ID {task_id}.")

# Usuwanie wszystkich zadań
def delete_all_tasks():
    save_tasks([])
    print("Wszystkie zadania zostały usunięte.")

# Usuwanie wybranych zadań na podstawie listy ID
def delete_selected_tasks(tasks, ids_to_delete):
    tasks = [task for task in tasks if task["id"] not in ids_to_delete]
    # Aktualizacja ID zadań
    for i, task in enumerate(tasks):
        task["id"] = i + 1
    save_tasks(tasks)
    print(f"Usunięto zadania o ID: {ids_to_delete}. Zaktualizowano ID pozostałych zadań.")

# Przykładowe użycie
if __name__ == "__main__":
    tasks = load_tasks()

    # Dodawanie zadania
    add_task(tasks, "Kupić mleko", "wysoki", "2025-01-20", "10:00", "example@example.com")

    # Edycja zadania
    edit_task(tasks, 1, opis="Kupić mleko i chleb", godzina="11:00")

    # Usuwanie zadania
    delete_task(tasks, 1)

    # Usuwanie wszystkich zadań
    delete_all_tasks()

    # Dodawanie przykładowych zadań
    add_task(tasks, "Zadanie 1", "niski", "2025-01-15", "12:00", "test1@example.com")
    add_task(tasks, "Zadanie 2", "średni", "2025-01-16", "13:00", "test2@example.com")
    add_task(tasks, "Zadanie 3", "wysoki", "2025-01-17", "14:00", "test3@example.com")
    add_task(tasks, "Zadanie 4", "niski", "2025-01-18", "15:00", "test4@example.com")

    # Usuwanie wybranych zadań
    delete_selected_tasks(tasks, [2, 4])

    # Wczytanie wszystkich zadań
    print("Obecne zadania:", load_tasks())


