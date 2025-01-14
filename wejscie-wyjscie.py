import json 
from datetime import datetime

#Funkcja, która zapisuja zadania do pliku json
def save_tasks_to_json(tasks, filename="tasks.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        print(f"Zadania zostały zapisane do pliku: {filename}")
    except Exception as e:
        print(f"Błąd podczas zapisywania pliku JSON: {e}")
#Funkcja, która wczytuje zadania z pliku json i konwertuje na liste zadań
def load_tasks_from_json(filename="tasks.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            print(f"Zadania zostały wczytane z pliku: {filename}")
            return tasks
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje. Zwracam pustą listę.")
        return []
    except json.JSONDecodeError:
        print(f"Plik {filename} ma niepoprawny format JSON.")
        return []
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku JSON: {e}")
        return []
#Test 
if __name__ == "__main__":
    # Przykładowe dane
    tasks = [
        {
            "title": "Jedzenie",
            "description": "Kupić piergi w żabce",
            "due_date": "2025-01-15",
            "completed": False
        },
        {
            "title": "Nauka",
            "description": "Zrobić zadania z logiki na poniedzialek",
            "due_date": "2025-01-20",
            "completed": False
        },
    ]

    # Zapis do JSON
   # save_tasks_to_json(tasks)

    # Wczytanie z JSON
   # loaded_tasks_json = load_tasks_from_json()
print("Nig")   
