'''
THIS MODULE IS USED TO CONNECT TO DB via MongoDB
'''
from pymongo import MongoClient

'''
Using Mongodb to store Data:
My DB named "DoorLock" has two Collections:
    + Users: store userInfo(_id, name, priority).
    + History: store userEvent(add new user, remove user).
CONNECTING STRING FORM: "mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<user>?ssl=true&ssl_cert_reqs=CERT_NONE"
'''
# connect to DB
cluster = MongoClient("mongodb+srv://duyvu1109:duyvu1109@cluster0.jzoff.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
# open DoorLock
db = cluster["DoorLock"]
# open User collection
users = db["User"]
# open History collection
history = db ["History"]
