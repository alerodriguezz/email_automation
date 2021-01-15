#!/usr/bin/env python3

import smtplib
import os,sys
import email.utils
import dotenv
from email.mime.text import MIMEText
from dotenv import load_dotenv

#load variables set in your .env file
load_dotenv()

#which email is this being sent from?
sender_email = str(os.getenv('SENDER_EMAIL'))
sender_name = "John"

#pass for sender's account 
password = str(os.getenv('PASSWORD'))
"""
emails=[]
names=[]
#retreive email list 
with open(os.path.join(sys.path[0], "Email_List.csv"), "r") as f:
    temp = f.readlines()[1:]

    for i in temp:
        names.append(i.split()[0] + " " + i.split()[1])
        emails.append(i.split()[2])
        
    f.close()

email_list=list(zip(names,emails))
"""

#who is this mail going to be sent to 
recipient_email=str(os.getenv('RECIPIENT_EMAIL'))
recipient_name= "Sterling"

#retreive email content

email_html=""
with open(os.path.join(sys.path[0], "Email_Contents.html"), "r") as f:
    temp = f.read()
    email_html += temp
    f.close()

#a loop can be incorporated into this def to broadcast to a larger audience
# e.g for name, email in zip(name_list, email_list)....

def send_email():
    print("Sending email...\n")

    message = MIMEText(email_html, 'html')
    #message.add_header('Content-Type','text/html')
    
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