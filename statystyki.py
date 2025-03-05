import json
from datetime import datetime

class TaskStats:
    #otwieranie pliku .json
    def __init__(self,file):
        with open(file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)["zadania"]  # Zakładając, że dane są w kluczu "zadania"
    #iteruje przez zadania z pliku i zlicza wg statusu
    def update(self, file=None):
        if file is None:
            file = self.file
        with open(file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)["zadania"]
    def c_by_status(self):
        status_c = {}
        for task in self.data:
            if task["status"] not in status_c:
                status_c[task["status"]] = 1
            else:
                status_c[task["status"]] += 1
        
        return status_c
    
    #iteruje przez zadania z pliku i zlicza wg kategorii
    def c_by_categories(self):
        categories_c = {}
        for task in self.data:
            if task["kategoria"] in categories_c:
                categories_c[task["kategoria"]] += 1
            else:
                categories_c[task["kategoria"]] = 1
        return categories_c
    
    #zlicza ile jeszcze zadan mamy do zrobienia w okreslonym czasie
    def close_to_deadline(self):
        current_date = datetime.now().date()
        current_week = current_date.isocalendar()[1] #numer obecnego tygodnia
        deadline = {"dzisiaj":0,"jutro": 0, "ten tydzień": 0 }

        for task in self.data:
            task_deadline = task["termin"]
            task_deadline = datetime.strptime(task_deadline,"%Y-%m-%d").date()
            task_week = task_deadline.isocalendar()[1]
            how_many_days = (task_deadline - current_date).days
            if how_many_days == 0 and task["status"] == "not completed":
                deadline["dzisiaj"] += 1
            if how_many_days == 1 and task["status"] == "not completed":
                deadline["jutro"] += 1
            if task_week == current_week and task["status"] == "not completed":
                deadline["ten tydzień"] += 1
        return deadline
    
# funkcja zapisuje jak duzo wykonujemy zadan z roznych kategorii
def global_stats(plik,kategoria):
    with open(plik, "r",encoding="utf-8") as file:
        data = json.load(file)
    
    if kategoria.lower() in data:
        data[kategoria.lower()] += 1
    else:
        data[kategoria.lower()] = 1
    with open(plik, "w") as file:
        json.dump(data, file, indent=4)
# wylicza procentowo jak duzo zadan kazdej kategorii wykonalismy
def percentage(plik):
    with open(plik, "r",encoding="utf-8") as file:
        data = json.load(file)["zadania"]
    sum = 0
    per = {}
    for category in data:
        sum += data[category]
    for category in data:
        per[category] = int(100 * data[category] / sum)
        print(category + ": " + str(per[category])+"%")


# test = TaskStats("tasks.json")
# #test
# print(test.close_to_deadline())
# print(test.c_by_categories())
# print(test.c_by_status())
# percentage("stats.json")


