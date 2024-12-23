import json


class FiltrySortowanie:

    def __init__(self, file_name):
        '''
        :param file_name: Nazwa pliku
        '''
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                plik = json.load(file)
                self.tasks = plik['zadania']

            if not isinstance(self.tasks, list):
                raise ValueError('Plik powinien zawierać listę zadań!')

        except FileNotFoundError:
            raise FileNotFoundError(f'Nie znaleziono pliku o nazwie {file_name}')

    def sort_tasks(self, key, reverse):
        '''
        :param key: Klucz, wedle którego będziemy sortować nasz plik
        :param reverse: Wartość, która mówi czy sortujemy rosnąco lub malejąco
        :return: Zwraca posortowany słownik
        '''
        return sorted(self.tasks, key=lambda task: task[key], reverse=reverse)

    def filter_tasks_by_date(self, start, end):
        '''
        :param start: Początek daty
        :param end: Koniec daty
        :return: Zwraca wartości w podanym przedziale daty
        '''
        return [task for task in self.tasks if start <= task['termin'] <= end]

    def filter_tasks(self, value, key):
        '''
        :param value: Co będziemy filtrować
        :param key: Warunek, po którym będziemy filtrować
        :return: Zwraca przefiltrowany plik
        '''
        return [task for task in self.tasks if task.get(value) == key]

filtr = FiltrySortowanie('tasks.json')
filter = filtr.filter_tasks('priorytet', 'wysoki')
print("Posortowane zadania:", filter)