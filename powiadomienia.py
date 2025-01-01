### Powiadomienia ###
import smtplib
from email.utils import formataddr
from email.mime.text import MIMEText
import datetime as dt
import json
my_email = "t0.d0.l1st.pwi@gmail.com"
app_password = "oidg goxj cgci nqrp"
file_path = "tasks.json"

class SendingReminder:
    def __init__(self, my_email, app_password, user_email):
        self.my_email = my_email
        self.app_password = app_password
        self.user_email = user_email


        # set a time to send a reminder#
        # set a time to send a reminder#

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
    def send_email(self, subject, message, color):
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
                msg['To'] = self.user_email

                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=[self.user_email],
                    msg=msg.as_string()
                )
            print("Email sent!")
        except Exception as e:
            print(f"Wystąpił błąd podczas wysyłania e-maila: {e}")

    # Sending Reminders #
    def check_and_send_reminders(self, file_path):
        ###Sprawdza terminy zadań i wysyła przypomnienia dla zadań z dzisiejszą datą.###
        tasks_data = self.read_tasks(file_path)


        today = dt.date.today().isoformat()
        print(f"Dzisiejsza data: {today}")

        zadania = tasks_data.get('zadania', [])
        for zadanie in zadania:
            termin = zadanie.get("termin")
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
            if termin == today:
                print(f"Wysyłanie przypomnienia dla zadania: {opis}")
                message_body = f"""
                Zadanie: <b>{opis}</b><br>
                Data: <i>{termin}</i>
                """
                self.send_email(subject=priorytet, message=message_body, color=color)


## test ##

if __name__ == "__main__":
    my_email = "t0.d0.l1st.pwi@gmail.com"
    app_password = "oidg goxj cgci nqrp"
    user_email = "wo.playstation@gmail.com"

    reminder = SendingReminder(my_email, app_password, user_email)
    reminder.check_and_send_reminders("tasks.json")



