'''
THIS MODULE IS USED TO CONNECT TO DB via MongoDB
'''
from pymongo import MongoClient
import os
'''
Using Mongodb to store Data:
My DB named "DoorLock" has two Collections:
    + Users: store userInfo(_id, name, priority).
    + History: store userEvent(add new user, remove user).
CONNECTING STRING FORM: "mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<user>?ssl=true&ssl_cert_reqs=CERT_NONE"
'''
# connect to DB
cluster = MongoClient("mongodb+srv://duyvu1109:Duyvu1109@cluster0.jzoff.mongodb.net/DoorLock?ssl=true&ssl_cert_reqs=CERT_NONE")
# open DoorLock
db = cluster["DoorLock"]
# open User collection
users = db["User"]
# open History collection
history = db["History"]

def queryFromDB():
    if not os.path.exists('users.json') and not os.path.exists('history.json'):
        open('users.json', 'a').close()
        open('history.json', 'a').close()
    from bson.json_util import dumps
    UsersData = users.find()
    HistoryData = history.find()
    listUser = list(UsersData)
    listHistory = list(HistoryData)
    # Converting to the JSON
    json_data = dumps(listUser, indent = 2) 
    with open('users.json', 'w') as file:
        file.write(json_data)
    file.close()
    json_data = dumps(listHistory, indent = 2) 
    with open('history.json', 'w') as file:
        file.write(json_data)
    file.close()