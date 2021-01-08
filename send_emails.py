#!/usr/bin/env python3

import smtplib
import os 

#which email is this being sent from?
sender_email = str(os.environ.get('SENDER_EMAIL'))

#pass for sender's account 
password = str(os.environ.get('PASSWORD'))

#who is this mail going to be sent to 
recipient_email='alex4dodgers@yahoo.com'

#email context

email_text='''
Hello there. 
'''
def send_email():
    
    #setup email server, email host , and common used port 
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    #encrypts smtp commands
    server.starttls()

    #Login to senders' email account 
    server.login(sender_email, password)

    #Send the email
    server.sendmail(sender_email, recipient_email, email_text)

    server.quit()
    pass

send_email()