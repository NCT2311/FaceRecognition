import mongodb
from face_reg import storeUserImage
from datetime import datetime
import shutil

class UserWork:
    def addUser(self):
        cur_id = mongodb.users.count_documents({})
        name = str(input("Type your name: "))
        while not self.existsUser(name):
            print("User already exists, try again!")
            name = str(input("Type your name: "))
        priority = int(input("Select priority: "))
        newUser = {"_id": cur_id, "name": name, "priority": priority}
        mongodb.users.insert_one(newUser)
        self.addHistoryEvent("add new user", cur_id, name)
        storeUserImage(name)

    def removeUser(self, name):
        mongodb.users.delete_one({'name': name})
        self.addHistoryEvent("remove user", name)
        shutil.rmtree('user_capture/' + str(name))
        print("done!")

    def addHistoryEvent(self, type, id, name):
        timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if (type == "add new user"):
            timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = name + ' added'
        elif (type == "remove user"):
            message = name + ' removed'
        post = {"_id": id, "time": timeEvent, "message": message}
        mongodb.history.insert_one(post)
    
    def removeHistory(self):
        mongodb.history.delete_many({})

    def existsUser(self, name):
        return mongodb.users.count_documents({"name": name}) == 0


if __name__ == '__main__':
    collection = UserWork()
    # collection.removeHistory()
    # collection.addUser()    # add new user
    collection.removeUser('eng tin')
    # collection.removeUser('vunguyenduy')
    # collection.removeHistory()
    mongodb.queryFromDB()
    
