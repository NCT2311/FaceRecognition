import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("duyvu1109@gmail.com", "**************")
server.sendmail("duyvu1109@gmail.com",
                "duyvu1109@gmail.com",
                "Hello, World!")
server.quit()