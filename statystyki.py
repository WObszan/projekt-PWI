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
        pass