import glob
import pandas as pd
import smtplib
import random
import datetime as dt

MY_EMAIL = "some_random_email@gmail.com"
PASSWORD = "some_random_password"

# ---------------------------- 💡💻 CHECK DAY 💻💡 -----------------------------
today = dt.datetime.now()
month = today.month
day = today.day
# ----------------------- 💡💻 CHECK FOR BIRTHDATE 💻💡 ------------------------
data = pd.read_csv('./birthdays.csv')
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)
data_dict = {index: value for (index, value) in data.iterrows()}
data_list = []
for x in data_dict.values():
    if x['month'] == month and x['day'] == day:
        data_list.append((x['name'], x['email']))
# ------------------------- 💡💻 CHECK TEMPLATES 💻💡 --------------------------
templates_list = [file for file in glob.glob('./letter_templates' + '/*')]
with open(random.choice(templates_list)) as file:
    text = file.read()
# ---------------------------- 💡💻 SEND EMAIL 💻💡 ----------------------------
if data_list:
    for x in data_list:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=x[1],
                    msg=("Subject:Happy Birthday\n\n"
                         f"{text.replace('[NAME]', x[0])}"
                         )
            )
