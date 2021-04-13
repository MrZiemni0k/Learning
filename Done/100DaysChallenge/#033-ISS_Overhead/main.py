import requests
import datetime as dt
import time
import smtplib

MY_LAT = 52.165219
MY_LONG = 21.082282
parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0, }
MY_EMAIL = 'some_random_mail@gmail.com'
MY_PASSWORD = 'some_random_password'


def is_iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)


def check_if_dark():
    if is_iss_visible():
        response = requests.get("https://api.sunrise-sunset.org/json",
                                params=parameters
                                )
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = dt.datetime.now().hour
        return sunrise >= time_now or sunset <= time_now
    return False


def send_email():
    if check_if_dark():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=('Subject:ISS NOTIFICATION\n\n'
                                     'Look up!\nISS is coming.')
                                )


while True:
    send_email()
    time.sleep(60)

