import mongodb
from face_reg import storeUserImage
from datetime import datetime

class UserWork:
    def addUser(self):
        cur_id = mongodb.users.count_documents({})
        name = str(input("Type your name: "))
        priority = int(input("Select priority: "))
        newUser = {"_id": cur_id, "name": name, "priority": priority}
        mongodb.users.insert_one(newUser)
        self.addHistoryEvent("add new user", name)
        storeUserImage(name)

    def removeUser(self, name):
        mongodb.users.delete_one({'name': name})
        self.addHistoryEvent("remove user", name)
        print("done!")

    def addHistoryEvent(self, type, name):
        timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if (type == "add new user"):
            timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = name + ' added'
        elif (type == "remove user"):
            message = name + ' removed'
        post = {"_time": timeEvent, "message": message}
        mongodb.history.insert_one(post)
    
    def removeHistory(self):
        mongodb.history.delete_many({})
        
if __name__ == '__main__':
    collection = UserWork()
    collection.addUser()    # add new user
    
