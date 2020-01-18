import smtplib
from random import randint

sender = 'postmaster@sandbox600176f7c3a847a88dd5ad926c534a9e.mailgun.org'
sender_password = '7e95f9ed54cecd6bdde64f67e8d6065a-0a4b0c40-5a4003e7'

server = 'smtp.mailgun.org', 587
smtpObj = smtplib.SMTP(server[0], server[1])
smtpObj.starttls()
smtpObj.login(sender, sender_password)


def send_email(email):
    code = randint(1000, 10000)
    smtpObj.sendmail(sender, email, "Your code is " + str(code))

    return code

###it is test
#send_email('kesha787898@gmail.com')
