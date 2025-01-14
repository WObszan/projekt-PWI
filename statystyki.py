import json
from datetime import datetime

class TaskStats:
    def __init__(self,file):
        with open(file, 'r', encoding='utf-8') as file:
            self.data = json.load(file)["zadania"]
    
    def c_by_status(self):
        status_c = {"do_zrobienia": 0, "w_trakcie": 0, "zrobione": 0}
        for task in self.data:
            status_c[task["status"]] += 1
        
        return status_c
    
    def c_by_categories(self):
        categories_c = {"dom":0, "studia": 0}
        for task in self.data:
            categories_c[task["kategoria"]] += 1

        return categories_c
    def close_to_deadline(self):
        current_date = datetime.now().date()
        deadline = {"do dzisiaj":0,"do jutra": 0, "w tym tygodniu": 0 }

        for task in self.data:
            task_deadline = task["termin"]
            task_deadline = datetime.strptime(task_deadline,"%Y-%m-%d").date()
            how_many_days = (task_deadline - current_date).days

            if how_many_days == 0:
                deadline["do dzisiaj"] += 1
                deadline["w tym tygodniu"] += 1
            if how_many_days == 1:
                deadline["do jutra"] += 1
                deadline["w tym tygodniu"] += 1
            if how_many_days >= 2 and how_many_days < 7:
                deadline["w tym tygodniu"] += 1
