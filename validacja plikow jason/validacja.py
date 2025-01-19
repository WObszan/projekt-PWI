import json
from datetime import datetime
import re

class TaskValidator:
    def __init__(self, tasks):
        self.tasks = tasks
        self.errors = []

    def validate(self):
        self.errors.clear()
        for task in self.tasks:
            self.validate_task(task)
        if self.errors:
            print("Walidacja nie powiodła się. Znaleziono błędy:")
            for error in self.errors:
                print(f"- {error}")
            return False
        print("Wszystkie zadania są poprawne.")
        return True

    def validate_task(self, task):
        task_id = task.get("id", "Nieznany ID")
        required_fields = ["id", "opis", "priorytet", "termin", "godzina", "email", "zrobione"]
        for field in required_fields:
            if field not in task:
                self.errors.append(f"Zadanie ID {task_id}: brakujące pole '{field}'.")
        if any(field not in task for field in required_fields):
            return
        if not isinstance(task["id"], int):
            self.errors.append(f"Zadanie ID {task_id}: pole 'id' musi być liczbą całkowitą.")
        if not self.validate_date(task["termin"]):
            self.errors.append(f"Zadanie ID {task_id}: nieprawidłowy format daty w 'termin' (oczekiwany YYYY-MM-DD).")
        if not self.validate_time(task["godzina"]):
            self.errors.append(f"Zadanie ID {task_id}: nieprawidłowy format godziny w 'godzina' (oczekiwany HH:MM).")
        if not self.validate_email(task["email"]):
            self.errors.append(f"Zadanie ID {task_id}: nieprawidłowy format email w 'email'.")
        if task["priorytet"] not in ["wysoki", "średni", "niski"]:
            self.errors.append(f"Zadanie ID {task_id}: nieprawidłowa wartość 'priorytet' (oczekiwane 'wysoki', 'średni', 'niski').")
        if task["zrobione"] not in ["Tak", "Nie"]:
            self.errors.append(f"Zadanie ID {task_id}: nieprawidłowa wartość 'zrobione' (oczekiwane 'Tak' lub 'Nie').")

    def validate_email(self, email):
        email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
        return re.match(email_pattern, email) is not None

    def validate_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_time(self, time):
        try:
            datetime.strptime(time, "%H:%M")
            return True
        except ValueError:
            return False
print("work")
