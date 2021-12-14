from pymongo import MongoClient
from email.mime.text import MIMEText
from datetime import datetime
import threading
import os, glob
import smtplib, ssl
'''
Using Mongodb to store Data:
My DB named "DoorLock" has two Collections:
    + Persons:  store person info.
    + Turn:     store history.
    + Flag:     store flag.
    + Users:
CONNECTING STRING FORM: "mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<user>?ssl=true&ssl_cert_reqs=CERT_NONE"
'''

cluster = MongoClient("mongodb+srv://hda1010:duyanh123@cluster0.ukowb.mongodb.net/facerecognition?retryWrites=true&w=majority")
# go to database
db = cluster["facerecognition"]

persons = db["persons"]
turns = db["turns"]
flag = db["flags"]

class Mongo:
    def updateFlag(self):
        f = flag.find_one()
        newFlag = {"$set":{"Flagcheck": True}}
        flag.update_one(f, newFlag)

    def clearTurn(self):
        turns.delete_many({})
        return 'delete all turns'

    def clearPerson(self):
        persons.delete_many({})
        return "Delete all persons"
    
    def getNameById(self, id):
        Fname, Lname = "",""
        for person in persons.find():
            if str(person['_id']) == id:
                Fname, Lname = person['Fname'], person['Lname']
        return Fname, Lname
###########################################################################################################
class Control:
    def addPerson(self, Fname, Lname, status=True):
        id = persons.count_documents({})
        createAt, updateAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newPerson = {
            "id": id,
            "Fname": Fname,
            "Lname": Lname,
            "Status": status,
            "createAt": createAt,
            "updateAt": updateAt,
            "__v": 0,
        }
        persons.insert_one(newPerson)

    def addTurn(self, imgUrl, Personid, __v, Status = True, Response = False):
        timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newTurn = {
            "urlimg": imgUrl, 
            "Status": Status, 
            "Personid": Personid, 
            "createAt": timeEvent, 
            "__v": __v, 
            "Response": Response
        }
        turns.insert_one(newTurn)

    # get imgUrl
    def getImageUrl(self):
        files = glob.glob('..\public\img\*.png')
        imgName = max(files, key=os.path.getctime)	
        imgUrl = "../img/" + imgName[14::]
        return str(imgUrl)
###########################################################################################################
'''
    This module used to send email automatic via email-bot chat named "doorlock.bot",
    
    Email: doorlock.bot@gmail.com
    Password: datkll211
'''
def sendMail():
    port = 465
    sender = 'doorlock.bot@gmail.com'
    password = 'datkll211'

    '''Type your email'''
    recieve = 'duyvu1109@gmail.com'

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = MIMEText('''\
    <pre>
        Dear anh em 196,

        Detect a stranger who wants to enter your home. 
        Time: {0}.

        <a href={1}>Click here</a> for more infomation.

        Hometown.
    </pre>. 

    '''.format(time, 'https://localhost:3000'),'html')

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, str(msg))

    print("sent email!")

###########################################################################################################
timerCounter, response = 300, False
def getResponse(turnId):
    global timerCounter, response
    response = flag.find_one({})['Response']
    if (response == True):
        print("door opened")
        timerCounter = 300
        f = flag.find_one()
        newResponse = {"$set":{"Response": False}}
        flag.update_one(f, newResponse)
        for turn in turns.find():
            if str(turn['_id']) == turnId:
                newResponse = {"$set":{"Response": True}}
                turns.update_one(turn, newResponse)
                turnId = ""
                break
        return True
    elif (timerCounter < 0 or flag.find_one({})['Flagcheck'] == False):
        print("door closed")
        timerCounter = 300
        return False
    else:
        timerCounter -= 1
    threading.Timer(1, getResponse, args=(turnId,)).start()
