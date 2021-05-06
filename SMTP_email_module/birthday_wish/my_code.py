import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "saroj.pradhan1710@yahoo.com"
PASSWORD = "rdlgqpszjkzezkrg"

data = pd.read_csv("birthdays.csv")
list_data = data.to_dict(orient="records")
print(list_data)

now = dt.datetime.now()
birth_month = now.month
birth_day = now.day
print(birth_month , birth_day)
for name in list_data:

    if birth_day == name['day'] and birth_month == name['month']:
        if birth_day == 6 and birth_month == 5:
            file_path = f"letter_templates/letter_4.txt"
        else:
            # print("matched")
            file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            print(contents)
            contents = contents.replace("[NAME]", str(name['name']))
            print(name['name'])
            print(contents)

        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=name['email'], msg=f"Subject:Happy Birthday!\n\n{contents}")
            print("sent")
        print(name['email'])

