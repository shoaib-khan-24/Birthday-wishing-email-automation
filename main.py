import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "khanshoaib@gmail.com"
MY_PASSWORD = "12345"

now = dt.datetime.now()
today_month = now.month
today_day = now.day

data = pd.read_csv("birthdays.csv")
for index,info in data.iterrows():
    if info.month == today_month and info.day == today_day:
        bday_name = info["name"]
        bday_email = info.email

        random_num = random.randint(1,3)
        with open(f"letter_templates/letter_{random_num}.txt") as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace("[NAME]" , bday_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=bday_email,
                msg=f"Subject:HAPPY BIRTHDAY\n\n{letter_content}"
            )




