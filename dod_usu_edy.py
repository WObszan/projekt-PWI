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



# Przykładowe użycie
if __name__ == "__main__":
    tasks = load_tasks()

    # Dodawanie zadania
    add_task(tasks, "Kupić mleko", "wysoki", "2025-01-20", "10:00", "example@example.com")
    # Edycja zadania
    edit_task(tasks, 1, opis="Kupić mleko i chleb", godzina="11:00")
    # Usuwanie zadania
    
    print("Obecne zadania:", load_tasks())


