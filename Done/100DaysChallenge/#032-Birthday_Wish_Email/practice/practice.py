import smtplib
import random
import datetime as dt

MY_EMAIL = "some_random_email@gmail.com"
PASSWORD = "some_random_password"

# --------------------------- 💡💻 CLEAN QUOTES 💻💡 ---------------------------
with open('./quotes.txt', encoding='utf8') as file:
    quotes_list = file.readlines()
    quotes_list = [x for x in quotes_list if x != '\n']
# --------------------------- 💡💻 CHOOSE QUOTE 💻💡 ---------------------------
index_quote = random.randrange(0, len(quotes_list), 2)
quote = quotes_list[index_quote] + quotes_list[index_quote + 1]
# ---------------------------- 💡💻 SEND QUOTE 💻💡 ----------------------------
now = dt.datetime.now().weekday()
if now == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Weekly Quote\n\n{quote}".encode('utf8')
        )
