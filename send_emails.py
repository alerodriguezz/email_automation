#!/usr/bin/env python3

import smtplib
import os
import email.utils
import dotenv
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

#which email is this being sent from?
sender_email = str(os.getenv('SENDER_EMAIL'))
sender_name = "John"

#pass for sender's account 
password = str(os.getenv('PASSWORD'))

#who is this mail going to be sent to 
recipient_email=str(os.getenv('RECIPIENT_EMAIL'))
recipient_name= "Sterling"

#email context

email_html='''
<h1> Hello, Customer</h1>
<p>Thank you for you purchase</p>
'''

#a loop can be incorporated into this def to broadcast to a larger audience
# e.g for name, email in zip(name_list, email_list)....

def send_email():
    print("Sending email...\n")

    message = MIMEText(email_html, 'html')
    #message.add_header('Content-Type','text/html')

    print (message)
    
    #Populate message object with data
    message['To'] = email.utils.formataddr((recipient_name,recipient_email))
    message['From'] = email.utils.formataddr((sender_name,sender_email))
    message['Subject'] = "New email with html functionality"
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