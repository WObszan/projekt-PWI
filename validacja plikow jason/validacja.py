import json
from datetime import datetime
class TaskValidator:
	def __init__(self,tasks):
		self.tasks=tasks
		self.errors=[]
	def validate(self):
		#Funkcja która sprawdza czy wszystkie taski na liscie sa poprawnie zapisane
	def validate_tasks(self,task):
		#funkcja ktora sprawdza pojedyncze zadanie czy jest poprawne
	def validate_email(self,email):
		#Funkcja ktora sprawdza czy email jest poprawnie zapisany 
		email_pattern = r"^[^@]+@[^@]+\.[^@]+$"
        return re.match(email_pattern, email) is not None
    def validate_date(self,date):
        #funkcja sprawdza czy data jest w poprawnym formacie
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    def validate_time(self,time):
        #funkcja sprawdza czy godzina jest w poprawnym formacie
        try:
            datetime.strptime(time_text, "%H:%M")
            return True
        except ValueError:
            return False

	
		
