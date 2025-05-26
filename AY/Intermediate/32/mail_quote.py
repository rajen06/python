import smtplib
import datetime as dt
import random

my_email = "bagh5@gmail.com"
password = " ybgf jonw"

def send_email(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="mailc@gmail.com", msg=f"Subject:Quote of the Day\n\n{quote}")


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        send_email(quote)
