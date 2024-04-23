import smtplib
import datetime as dt
import random

now = dt.datetime.now()
current_day = now.weekday()

l1 =  open("Base/Projects/Day 32/quotes.txt").readlines()
my_mail = "adhnanjeff26@gmail.com"
password = "mltanulztjluvnjk"
to_mail = "adhnanjeffms@gmail.com"
random_quote = random.choice(l1)

if current_day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #Makes the connection secure
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, 
                    to_addrs=to_mail, 
                    msg=f"Subject: Monday Motivation\n\nGood Morning Adhnan Jeff\n\n{random_quote}"
                    )
