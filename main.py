import mongodb
from datetime import datetime
import shutil
from time import sleep
from mail_sending import sendMail
import os
import glob

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
        createAt, updateAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newPerson = {"id": id, "Fname": Fname, "Lname": Lname, "Status": False, "createAt": createAt, "updateAt": updateAt, "__v": 0}
        mongodb.persons.insert_one(newPerson)

    def addTurn(self, id, urlimg, Status, Personid, __v):
        timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newPost = {"urlimg": urlimg, "Status": Status, "Personid": Personid, "createAt": timeEvent, "__v": __v}
        mongodb.turns.insert_one(newPost)

# use for send imgUrl
def getImageUrl():
    files = glob.glob('capture\\*.png')
    imgName = max(files , key=os.path.getctime)	
    return str(imgName)

if __name__ == '__main__':
    collection = Excute()
    
    while True:
        '''Begin detect face, after that, get Name, ImageUrl, ID to continue'''

        '''After detection, continue...'''
        imgUrl = getImageUrl()
        personID = mongodb.searchByName(name='NoName')
        isPerson = False
        if (isPerson):
            collection.addTurn('bla', imgUrl, False, personID, 0)
        else:
            collection.addPerson('Fname', 'Lname')
            collection.addTurn('bla', imgUrl, False, personID, 0)
            sendMail('https://linkToResponse.')
            mongodb.receiveResponse()

        pass

    
    
