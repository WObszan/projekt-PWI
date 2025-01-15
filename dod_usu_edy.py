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







# Przykładowe użycie
if __name__ == "__main__":
    tasks = load_tasks()

    
    
    
    
    print("Obecne zadania:", load_tasks())


