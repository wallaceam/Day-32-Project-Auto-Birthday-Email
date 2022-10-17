import random
import pandas
import smtplib
import datetime as dt

EMAIL = "allie@gmail.com"
PASSWORD = "1234abcd()"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()
}

if today in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        text = letter.read()
        text = text.replace("[NAME]", birthdays_dict[today]["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject: Happy Birthday!\n\n{text}")
