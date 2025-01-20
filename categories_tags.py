import json

class CategoryTagManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.categories = set()
        self.load_categories()

    def load_categories(self):
        """Wczytuje kategorie z pliku JSON."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for task in data["zadania"]:
                    self.categories.add(task["kategoria"])
        except FileNotFoundError:
            print(f"Plik {self.file_path} nie został znaleziony.")
        except json.JSONDecodeError:
            print(f"Plik {self.file_path} ma błędny format.")

    def add_category(self, name):
        """Dodaje nową kategorię do zbioru."""
        if not name or not name.strip():
            raise ValueError("Nazwa kategorii nie może być pusta.")
        if name in self.categories:
            print(f"Kategoria '{name}' już istnieje.")
        else:
            self.categories.add(name)
            self.save_categories()
            print(f"Kategoria '{name}' dodana.")

    def remove_category(self, name):
        """Usuwa kategorię, jeśli istnieje."""
        if name in self.categories:
            self.categories.remove(name)
            self.save_categories()
            print(f"Kategoria '{name}' została usunięta.")
        else:
            print(f"Kategoria '{name}' nie istnieje.")

    def save_categories(self):
        """Zapisuje kategorie do pliku JSON."""
        try:
            with open(self.file_path, 'r+', encoding='utf-8') as file:
                data = json.load(file)
                for category in self.categories:
                    if category not in data["zadania"]:
                        # Zaktualizuj plik o nowe kategorie
                        for task in data["zadania"]:
                            if task["kategoria"] == category:
                                task["kategoria"] = category
                file.seek(0)
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving categories: {e}")

    def view_categories(self):
        """Zwraca listę kategorii."""
        return list(self.categories)

    def add_tag(self, name):
        """Dodaje nowy tag."""
        if not name or not name.strip():
            raise ValueError("Nazwa tagu nie może być pusta.")
        if name in self.tags:
            print(f"Tag '{name}' już istnieje.")
        else:
            self.tags.add(name)
            print(f"Tag '{name}' dodany.")

    def remove_tag(self, name):
        """Usuwa tag, jeśli istnieje."""
        if name in self.tags:
            self.tags.remove(name)
            print(f"Tag '{name}' został usunięty.")
        else:
            print(f"Tag '{name}' nie istnieje.")

    def filter_tasks_by_category(self, tasks, category):
        """Filtruje zadania według kategorii."""
        if category not in self.categories:
            raise ValueError(f"Kategoria '{category}' nie istnieje.")
        return [task for task in tasks if task.get("category") == category]

    def filter_tasks_by_tag(self, tasks, tag):
        """Filtruje zadania według tagów."""
        if tag not in self.tags:
            raise ValueError(f"Tag '{tag}' nie istnieje.")
        return [task for task in tasks if tag in task.get("tags", [])]



