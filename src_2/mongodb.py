'''
THIS MODULE IS USED TO CONNECT TO DB via MongoDB
'''
from pymongo import MongoClient
import os
from time import sleep
'''
Using Mongodb to store Data:
My DB named "DoorLock" has two Collections:
    + Users: store userInfo(_id, name, priority).
    + History: store userEvent(add new user, remove user).
CONNECTING STRING FORM: "mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<user>?ssl=true&ssl_cert_reqs=CERT_NONE"
'''

# connect to DB
cluster = MongoClient("mongodb+srv://hda1010:duyanh123@cluster0.ukowb.mongodb.net/facerecognition?retryWrites=true&w=majority")
# open DoorLock
db = cluster["facerecognition"]
# open User collection
persons = db["persons"]
# open History collection
turns = db["turns"]

#

def queryFromDB():
    if not os.path.exists('users.json') and not os.path.exists('history.json'):
        open('persons.json', 'a').close()
        open('turns.json', 'a').close()
    from bson.json_util import dumps
    UsersData = persons.find()
    HistoryData = turns.find()
    listUser = list(UsersData)
    listHistory = list(HistoryData)
    # Converting to the JSON
    json_data = dumps(listUser, indent = 2) 
    with open('persons.json', 'w') as file:
        file.write(json_data)
    file.close()
    json_data = dumps(listHistory, indent = 2) 
    with open('turns.json', 'w') as file:
        file.write(json_data)
    file.close()

# queryFromDB()

# get response from DB
def receiveResponse():
    response = False
    for timeRemain in range(60):
        '''Query from DB to get response'''
        response = turns.find_one({}, {id: 0}).response
        if (response):
            return '''Door open'''
        sleep(5)
    return '''Door still lock'''

# get Person ID
def searchByName(name):
    for entry in persons.find():
        if entry.name == name:
            return entry.get('_id')
    return '''Can't find'''

# open Flag collection
turns = db["flags"]
def updateFlag():
    
    pass