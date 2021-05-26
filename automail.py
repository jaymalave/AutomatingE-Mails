import datetime as dt
from datetime import datetime
import time
import smtplib


def send_mail():
    global send_time

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('jay.malave73@gmail.com', 'shhh, secret!')

        subject = 'Gmail Automation using Python'

        body = 'This mail was sent by a Python bot developed by Jay as he is quite lazy to do it by himself :)'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail('jay.malave73@gmail.com', 'jay.malave73@gmail.com', msg)
    # smtp.sendmail('jay.malave73@gmail.com', 'avishrodrigues@gmail.com', msg)
    # smtp.sendmail('jay.malave73@gmail.com', 'usha.malave81@gmail.com', msg)
    # smtp.sendmail('jay.malave73@gmail.com', 'anujs.joshi10@gmail.com', msg)
    # smtp.sendmail('jay.malave73@gmail.com', 'ishaarane@gmail.com', msg)


while True:
    send_mail()
    time.sleep(60)




