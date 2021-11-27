'''
    This module used to send email automatic via email-bot chat named "doorlock.bot",
    
    Email: doorlock.bot@gmail.com
    Password: datkll211
'''
import smtplib, ssl
from email.mime.text import MIMEText

def sendMail(link):
    port = 465

    sender = 'doorlock.bot@gmail.com'
    password = 'datkll211'

    '''Type your email'''
    recieve = 'duyvu1109@gmail.com'

    msg = MIMEText(u'Someone is coming, <a href={0}>click here</a> for more infomation'.format(link),'html')

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, str(msg))

    print("sent email!")

sendMail("https://localhost:3000")