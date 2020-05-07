import smtplib
import os 

#which email is this being sent from?
sender_email = os.environ.get('SENDER_EMAIL')

#pass for sender's account 
password = os.environ.get('PASSWORD')

#who is this mail going to be sent to 
recipient_email='archer.al@mail.com'

#email context

email_text='''
Hello there. 
'''
def send_email():
    
    #setup email server, email host , and common used port 
    server = smtplib.SMTP('smtp.mail.com',587)
    
    #encrypts smtp commands
    server.starttls()
    
    #Login to senders' email account 
    server.login(sender_email, password)

    #
    server.sendmail(sender_email, recipient_email, email_text)

    server.quit()
    pass

send_email()