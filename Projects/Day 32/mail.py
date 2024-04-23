#Automated Birthday wisher

import smtplib

my_email = "adhnanjeff26@gmail.com"
pass_word = "mltanulztjluvnjk"
to_mail = "amv.k.2712005@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #Makes the connection secure
    connection.login(user=my_email, password=pass_word)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=to_mail, 
                        msg="This is the body of my mail"
                        ) 
    


