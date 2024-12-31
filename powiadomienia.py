### Powiadomienia ###
import smtplib
my_email = "t0.d0.l1st.pwi@gmail.com"
app_password = "oidg goxj cgci nqrp"
user_mail = "wo.playstation@gmail.com"
message = "Test"
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user= my_email, password=app_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=user_mail,
        msg=f"Subject:Reminder\n\n {message}"
    )