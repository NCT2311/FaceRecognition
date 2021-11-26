import mongodb
from datetime import datetime
from time import sleep
from mail_sending import sendMail
import os
import glob

class Excute:
    # using for stranger
    def addPerson(self, Fname, Lname):
        id = mongodb.persons.count_documents({})
        createAt, updateAt = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ), datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        newPerson = {
            "id": id,
            "Fname": Fname,
            "Lname": Lname,
            "Status": False,
            "createAt": createAt,
            "updateAt": updateAt,
            "__v": 0,
        }
        mongodb.persons.insert_one(newPerson)

    def addTurn(self, urlimg, Status, Personid, __v, Response = False):
        timeEvent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        newPost = {"_id": 99,"urlimg": urlimg, "Status": Status, "Personid": Personid, "createAt": timeEvent, "__v": __v, "Response": Response}
        mongodb.turns.insert_one(newPost)


# get imgUrl
"../img/logo.png"
def getImageUrl():
    files = glob.glob('public\img\*.png')
    imgName = max(files ,key=os.path.getctime)	
    imgUrl = "../img/" + imgName[11::]
    return str(imgUrl)



if __name__ == "__main__":
    collection = Excute()
    collection.addTurn(getImageUrl(), False, 'ok eng DA', 0, True)
    # collection.addPerson('Undefined', 'Undefined')

    # while True:
    #     '''Begin detect face, after that, get Name, ImageUrl, ID to continue'''
        
    #     '''After detection, continue...'''
    #     imgUrl = getImageUrl()
    #     personID = mongodb.searchByName(name='NoName')
    #     isPerson = False
    #     if (isPerson):
    #         collection.addTurn('bla', imgUrl, False, personID, 0)
    #     else:
    #         # add new person to Person Collection   
    #         collection.addPerson('Fname', 'Lname')
    #         # add new Turn
    #         collection.addTurn('bla', imgUrl, False, personID, 0)
    #         sendMail('https://linkToResponse.')
    #         mongodb.receiveResponse()

    #     pass

    
    
