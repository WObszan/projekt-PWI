class FiltrySortowanie:

    def __init__(self, file_name):
        '''
        :param file_name: Nazwa pliku
        '''
        with open(file_name, 'r') as file:
            self.tasks = file.readlines()

    def sort_tasks(self, key, reverse):
        '''
        :param key: Klucz, wedle którego będziemy sortować nasz plik
        :param reverse: Wartość, która mówi czy sortujemy rosnąco lub malejąco
        :return: Zwraca posortowany słownik
        '''
        return sorted(self.tasks, key=lambda task: task[key], reverse=reverse)


