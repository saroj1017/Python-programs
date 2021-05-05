import smtplib
import datetime as dt
import random

MY_EMAIL = "fahrancarona@gmail.com"   # use you own email id , currently this won't work
PASSWORD = "Randomaccount@10"
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}".encode('utf-8')
                            )
