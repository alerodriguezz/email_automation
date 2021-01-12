#!/usr/bin/env python3

import smtplib
import os
import email.utils
from email.mime.text import MIMEText

#which email is this being sent from?
sender_email = str(os.environ.get('SENDER_EMAIL'))
sender_name = "John"

#pass for sender's account 
password = str(os.environ.get('PASSWORD'))

#who is this mail going to be sent to 
recipient_email='alex4dodgers@yahoo.com'
recipient_name= "Sterling"

#email context

email_text='''
Hello there. Again.
'''
def send_email():
    print("Sending email...\n")

    message = MIMEText(email_text)
    
    #Populate message object with data
    message['To'] = email.utils.formataddr((recipient_name,recipient_email))
    message['From'] = email.utils.formataddr((sender_name,sender_email))
    message['Subject'] = "Test email"
    #setup email server, email host , and common used port 
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    #encrypts smtp commands
    server.starttls()

    #Login to senders' email account 
    server.login(sender_email, password)

    #Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())

    server.quit()
    pass
    print("Email Sent. \n")
send_email()