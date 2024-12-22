class FiltrySortowanie:

    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self.tasks = file.readlines()

    def sort_by_date(self, key):
