import pymongo
import mongodb
from datetime import datetime
import shutil
from time import sleep
from mail_sending import sendMail

class Excute:
    # def removeUser(self, name):
    #     mongodb.persons.delete_one({'name': name})
    #     self.addHistoryEvent("remove user", name)
    #     shutil.rmtree('user_capture/' + str(name))
    #     print("done!")
    
    # def removeHistory(self):
    #     mongodb.turns.delete_many({})

    # def existsUser(self, name):
    #     return mongodb.persons.count_documents({"name": name}) == 0

    # using for stranger
    def addPerson(self, Fname, Lname):
        id = mongodb.persons.count_documents({})
        Fname = Fname
        Lname = Lname
        createAt, updateAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newPerson = {"id": id, "Fname": Fname, "Lname": Lname, "Status": False, "createAt": createAt, "updateAt": updateAt, "__v": 0}
        mongodb.persons.insert_one(newPerson)

    def addTurn(self, id, urlimg, Status, Personid, __v):
        timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newPost = {"urlimg": urlimg, "Status": Status, "Personid": Personid, "createAt": timeEvent, "__v": __v}
        mongodb.turns.insert_one(newPost)

    def receiveResponse(self, responseFromDB):
        '''Get response from DB'''
        for countdonw in range(60):
            if (responseFromDB):
                return '''Door open'''
            sleep(5)
        return '''Door still lock'''


if __name__ == '__main__':
    collection = Excute()
    
    while True:
        '''Begin detect face, after that, get Name, ImageUrl, ID to continue'''
        isPerson = False
        if (isPerson):
            collection.addTurn('bla', '/.png', False, 0, 0)
        else:
            collection.addPerson('Fname', 'Lname')
            collection.addTurn('bla', '/.png', False, 0, 0)
            sendMail('https://linkToResponse.')
        pass

    
    
