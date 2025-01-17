import json
from datetime import datetime

class TaskStats:
    def __init__(self,file):
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
    
    def c_by_categories(self):
        categories_c = {}
        for task in self.data:
            if task["kategoria"] in categories_c:
                categories_c[task["kategoria"]] += 1
            else:
                categories_c[task["kategoria"]] = 1
        return categories_c
    
    def close_to_deadline(self):
        current_date = datetime.now().date()
        current_week = current_date.isocalendar()[1] #numer obecnego tygodnia
        deadline = {"dzisiaj":0,"jutro": 0, "ten tydzień": 0 }

        for task in self.data:
            task_deadline = task["termin"]
            task_deadline = datetime.strptime(task_deadline,"%Y-%m-%d").date()
            task_week = task_deadline.isocalendar()[1]
            how_many_days = (task_deadline - current_date).days

            if how_many_days == 0:
                deadline["dzisiaj"] += 1
            if how_many_days == 1:
                deadline["jutro"] += 1
            if task_week == current_week:
                deadline["ten tydzień"] += 1
        return deadline

test = TaskStats("tasks.json")
#test
print(test.close_to_deadline())
print(test.c_by_categories())
print(test.c_by_status())