class CategoryTagManager:
    def __init__(self):
        self.categories = set()  # Zbiór, żeby uniknąć duplikatów
        self.tags = set()

    def add_category(self, name):
        """Dodaje nową kategorię."""
        if not name or not name.strip():
            raise ValueError("Nazwa kategorii nie może być pusta.")
        if name in self.categories:
            print(f"Kategoria '{name}' już istnieje.")
        else:
            self.categories.add(name)

            print(f"Kategoria '{name}' dodana.")

    def remove_category(self, name):
        """Usuwa kategorię, jeśli istnieje."""
        if name in self.categories:
            self.categories.remove(name)
            print(f"Kategoria '{name}' została usunięta.")
        else:
            print(f"Kategoria '{name}' nie istnieje.")

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



