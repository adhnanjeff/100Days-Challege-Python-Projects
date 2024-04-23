#Simple mail transfer protocol

import smtplib
my_email = "adhnanjeff26@gmail.com"
pass_word = "mltanulztjluvnjk"
to_mail = "adhnanjeffms@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com")

#Gmail - smtp.gmail.com
#Hotmail - smtp.live.com
#Yahoo - smtp.mail.yahoo.com
#iCloud - smtp.mail.me.com

connection.starttls()
# TLS - Transport layer security
"Used to encrypt mail so that no third person reads the mail"

#To login into our mail ID
connection.login(user=my_email, password=pass_word)

#To send mail to other person

#connection.sendmail(from_addr=my_email, to_addrs=to_mail, msg="Subject:Hello!\n\nThis is the body of my mail") 

#From address and to address is given
#If subject is not given the mail will be sent to spam folder
connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute
sec = now.second

print(year, month, day, hour, min, sec)

weekday = now.weekday()
date_of_birth = dt.datetime(year=2004, month=10, day=26)
