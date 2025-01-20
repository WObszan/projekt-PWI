import json 
from datetime import datetime

#Funkcja, która zapisuja zadania do pliku json
def save_tasks_to_json(tasks, filename="tasks.json"):
    try:
        data = {"zadania": tasks}
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Zadania zostały zapisane do pliku: {filename}")
    except Exception as e:
        print(f"Błąd podczas zapisywania pliku JSON: {e}")
#Funkcja, która wczytuje zadania z pliku json i konwertuje na liste zadań
def load_tasks_from_json(filename="tasks.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            tasks = data.get("zadania", [])
            print(f"Zadania zostały wczytane z pliku: {filename}")
            return tasks
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje. Zwracam pustą listę.")
        return []
    except json.JSONDecodeError as jde:
        print(f"Plik {filename} ma niepoprawny format JSON: {jde}")
        return []
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku JSON: {e}")
        return []
#Test 
if __name__ == "__main__":
    # Przykładowe dane
    tasks = [
        {
            "id": 1,
            "opis": "Zrobić zakupy spożywcze",
            "priorytet": "wysoki",
            "termin": "2024-12-24",
            "godzina": "13:45",
            "email": "schraderdavid@btcmod.com",
            "zrobione": "Nie"
        },
        {
            "id": 2,
            "opis": "Napisać raport kwartalny",
            "priorytet": "średni",
            "termin": "2024-12-31",
            "godzina": "17:15",
            "email": "xedax86671@chansd.com",
            "zrobione": "Tak"
        },
        {
            "id": 3,
            "opis": "Ułożyć plan na nowy projekt",
            "priorytet": "wysoki",
            "termin": "2025-01-14",
            "godzina": "19:53",
            "email": "wo.playstation@gmail.com",
            "zrobione": "Tak"
        },
        {
            "id": 4,
            "opis": "Przygotować prezentację na spotkanie",
            "priorytet": "wysoki",
            "termin": "2024-12-26",
            "godzina": "09:45",
            "email": "bartek.kowalski@gmail.com",
            "zrobione": "Nie"
        },
        {
            "id": 5,
            "opis": "Zarezerwować wakacje na lato",
            "priorytet": "niski",
            "termin": "2025-03-01",
            "godzina": "15:25",
            "email": "piotr.lewandowski@gmail.com",
            "zrobione": "Nie"
        },
        {
            "id": 6,
            "opis": "Zrobić przegląd samochodu",
            "priorytet": "wysoki",
            "termin": "2025-01-09",
            "godzina": "19:45",
            "email": "ronaldo.cr7@gmail.com",
            "zrobione": "Tak"
        }
    ]

    save_tasks_to_json(tasks, "tasks.json")
    
    # Wczytaj zadania z pliku JSON
    loaded_tasks = load_tasks_from_json("tasks.json")
    
    # Wyświetl wczytane zadania
    print("\nWczytane zadania:")
    for task in loaded_tasks:
        print(task)  
