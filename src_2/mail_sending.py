'''
    This module used to send email automatic via email-bot chat named "doorlock.bot",
    
    Email: doorlock.bot@gmail.com
    Password: datkll211
'''
import smtplib, ssl

def sendMail(link):
    port = 465

    sender = 'doorlock.bot@gmail.com'
    password = 'datkll211'

    recieve = 'duyvu1109@gmail.com'

    message = link

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("sent email!")