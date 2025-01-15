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





# Przykładowe użycie
if __name__ == "__main__":
    tasks = load_tasks()

    # Dodawanie zadania
    add_task(tasks, "Kupić mleko", "wysoki", "2025-01-20", "10:00", "example@example.com")
    
    
    
    print("Obecne zadania:", load_tasks())


