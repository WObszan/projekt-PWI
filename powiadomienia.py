### Powiadomienia ###
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
import datetime as dt
import json

import time
import threading
from dotenv import load_dotenv
import os

load_dotenv()

file_path = "tasks.json"

class SendingReminder:
    def __init__(self, file_path):
        self.my_email = os.getenv("MY_EMAIL")
        self.app_password = os.getenv("APP_PASSWORD")
        self.file_path = file_path



        # set a time to send a reminder#
        # set a time to send a reminder#

    def run_in_background(self, file_path):
        while True:
            self.check_and_send_reminders(file_path)
            time.sleep(60)


            
    def read_tasks(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Plik JSON nie został znaleziony!")
        except json.JSONDecodeError:
            print("Błąd dekodowania pliku JSON!")
        return None

    #sending mail#

    def send_email(self, subject, message, color, user_email):

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.app_password)

                # Tworzenie treści wiadomości jako HTML z kolorową wiadomością
                html_message = f"""
                <html>
                    <body>
                        <p style="color: {color}; font-size: 16px;">{message}</p>
                    </body>
                </html>
                """
                msg = MIMEText(html_message, "html", "utf-8")  # Ustawienie typu "html"
                msg['Subject'] = subject
                msg['From'] = formataddr(("To Do List", self.my_email))
                msg['To'] = user_email

                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=[user_email],

                    msg=msg.as_string()
                )
            print("Email sent!")
        except Exception as e:
            print(f"Wystąpił błąd podczas wysyłania e-maila: {e}")

    # Sending Reminders #
    def check_and_send_reminders(self, file_path):
        ###Sprawdza terminy zadań i wysyła przypomnienia dla zadań z dzisiejszą datą.###
        tasks_data = self.read_tasks(file_path)


        today = dt.date.today()
        tomorrow = today +  dt.timedelta(days=1)
        godz = dt.datetime.now().strftime("%H:%M")
        print(f"Dzisiejsza data: {today.isoformat()}")
        zadania = tasks_data.get('zadania', [])
        for zadanie in zadania:
            email = zadanie.get('email')
            termin = zadanie.get("termin")
            godzina = zadanie.get("godzina")

            opis = zadanie.get("opis")
            typ_priorytetu = zadanie.get("priorytet")
            if typ_priorytetu == "wysoki":
                priorytet = "[Wysoki priorytet] REMINDER:"
                color = "red"
            elif typ_priorytetu == "średni":
                priorytet = "[Średni priorytet] Reminder:"
                color = "orange"
            else:
                priorytet = "Reminder:"
                color = "green"

            if termin == today.isoformat() and godz == godzina:
                print(f"Wysyłanie przypomnienia dla zadania: {opis}")
                message_body = f"""
                Zadanie: <b>{opis}</b><br>
                Data: <i>{termin}</i>
                """

                self.send_email(subject=priorytet, message=message_body, color=color, user_email=email)
            if termin == tomorrow.isoformat() and typ_priorytetu == "wysoki":
                print(f"Wysyłanie przypomnienia dla jutrzejszego zadania: {opis}")
                message_body = f"""
                                Zadanie na jutro: <b>{opis}</b><br>
                                Data: <i>{termin}</i>
                                Godzina: <i>{godz}</i>
                                """
                self.send_email(subject=priorytet, message=message_body, color=color, user_email=email)



## test ##

if __name__ == "__main__":


    reminder = SendingReminder( file_path)

    thread = threading.Thread(target=reminder.run_in_background, args=(file_path,), daemon=True)
    thread.start()

    while True:
        time.sleep(1)

