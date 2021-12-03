from pymongo import MongoClient
import os, glob
from time import sleep
import smtplib, ssl
from email.mime.text import MIMEText
from datetime import datetime

"""
Using Mongodb to store Data:
My DB named "DoorLock" has two Collections:
    + Persons:  store person info.
    + Turn:     store history.
    + Flag:     store flag.
    + Users:
CONNECTING STRING FORM: "mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<user>?ssl=true&ssl_cert_reqs=CERT_NONE"
"""

cluster = MongoClient(
    "mongodb+srv://hda1010:duyanh123@cluster0.ukowb.mongodb.net/facerecognition?retryWrites=true&w=majority"
)
# go to database
db = cluster["facerecognition"]

persons = db["persons"]
turns = db["turns"]
flag = db["flags"]


class Mongo:
    def queryFromDB(self):
        if not os.path.exists("users.json") and not os.path.exists("history.json"):
            open("persons.json", "a").close()
            open("turns.json", "a").close()
        from bson.json_util import dumps

        UsersData = persons.find()
        HistoryData = turns.find()
        listUser = list(UsersData)
        listHistory = list(HistoryData)
        # Converting to the JSON
        json_data = dumps(listUser, indent=2)
        with open("persons.json", "w") as file:
            file.write(json_data)
        file.close()
        json_data = dumps(listHistory, indent=2)
        with open("turns.json", "w") as file:
            file.write(json_data)
        file.close()

    # get response from DB
    def receiveResponse(self):
        response = False
        for timeRemain in range(6):
            """Query from DB to get response"""
            response = flag.find_one({})["Response"]
            if response:
                return """Door open"""
            sleep(1)
        return """Door still lock"""

    def updateFlag(self):
        f = flag.find_one()
        newFlag = {"$set": {"Flagcheck": False}}
        flag.update_one(f, newFlag)

    def clearTurn(self):
        turns.delete_many({})
        return "delete all turns"

    def getNameById(self, id):
        Fname, Lname = "", ""
        for person in persons.find():
            if str(person["_id"]) == id:
                Fname, Lname = person["Fname"], person["Lname"]
        return Fname, Lname


###########################################################################################################
class Control:
    def addPerson(self, Fname, Lname, status=True):
        id = persons.count_documents({})
        createAt, updateAt = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ), datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

    def addTurn(self, urlimg, Status, Personid, __v, Response=False):
        timeEvent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newPost = {
            "urlimg": urlimg,
            "Status": Status,
            "Personid": Personid,
            "createAt": timeEvent,
            "__v": __v,
            "Response": Response,
        }
        turns.insert_one(newPost)

    # get imgUrl
    def getImageUrl(self):
        files = glob.glob("..\public\img\*.png")
        imgName = max(files, key=os.path.getctime)
        imgUrl = "../img/" + imgName[14::]
        return str(imgUrl)


###########################################################################################################
"""
    This module used to send email automatic via email-bot chat named "doorlock.bot",
    
    Email: doorlock.bot@gmail.com
    Password: datkll211
"""


def sendMail(link, Fname="Undefined", Lname="Undefined"):
    port = 465

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sender = "doorlock.bot@gmail.com"
    password = "datkll211"

    """Type your email"""
    recieve = "duyvu1109@gmail.com"

    submsg = """\
        <h2>{0} came home at {1} </h2>.
    """.format(
        Fname + Lname, time
    )

    msg = MIMEText(
        submsg
        + u"Someone is coming, <a href={0}>click here</a> for more infomation".format(
            link
        ),
        "html",
    )

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, str(msg))

    print("sent email!")


# sendMail('https://localhost:3000', Fname = 'ndvu', Lname = '')

###########################################################################################################
"""
    Another modules
"""
