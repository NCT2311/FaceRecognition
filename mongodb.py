from pymongo import MongoClient
from datetime import datetime



# "mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>/<user>?ssl=true&ssl_cert_reqs=CERT_NONE"
# connect string form

cluster = MongoClient("mongodb+srv://duyvu1109:duyvu1109@cluster0.jzoff.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE")
db = cluster["DoorLock"]
users = db["User"]
history = db ["History"]

# post = {"id": 1, "name": "duyvu", "priority": 1}
# post1 = {"id": 2, "name": "hda", "priority": 2}
# users.insert_one(post)
# users.insert_one(post1)

# users.delete_many({})
# history.delete_many({})
# print("Ready!")

# key = int(input())
# if (key == 1):
#     time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     print(time)
#     post = {"_id": 1, "name": "nguyenduyvu", "priority": 1}
#     h0 = {"_id": 1, "name": "nguyenduyvu", "time": time}
#     users.insert_one(post)
#     history.insert_one(h0)
