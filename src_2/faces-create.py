"""
This function will open webcam and start capture front_face's user
"""
import cv2
import os
<<<<<<< HEAD
import time


def storeUserImage(name):
=======
import pymongo
from modules import persons, Control

def newPerson():
    Fname = str(input("Type your first name: "))
    Lname = str(input("Type your last name: "))
    Control.addPerson(Fname, Lname, True)
    id = persons.find().sort('_id', pymongo.DESCENDING).limit(1)[0]['_id']
    # creater new directory in user_capture
    os.makedirs("./images/" + str(id))
    return 'Add {} to dataset'.format(Fname + Lname), str(id)

def storeUserImage():
    msg, newDataSet = newPerson()
    print(msg)
    print('Start create dataset...')
>>>>>>> Merge
    face_cascade = cv2.CascadeClassifier(
        "./cascades/data/haarcascade_frontalface_alt.xml"
    )
    video = cv2.VideoCapture(0)
    count = 0
<<<<<<< HEAD
    # creater new directory in user_capture
    os.makedirs("./images/" + str(name))
=======
>>>>>>> Merge
    while True:
        check, data = video.read()
        faces = face_cascade.detectMultiScale(data, scaleFactor=1.5, minNeighbors=5)
        for x, y, w, h in faces:
<<<<<<< HEAD
            # if count % 10 == 0:
            cv2.rectangle(data, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imwrite("./images/" + str(name) + "/" + str(count) + ".jpg", data)
=======
            # cv2.rectangle(data, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imwrite("./images/" + newDataSet + "/" + str(count) + ".jpg", data)
>>>>>>> Merge
            count += 1
        cv2.waitKey(3)
        cv2.imshow("Face Detect", data)
        key = cv2.waitKey(1)
<<<<<<< HEAD
        # Press 'q' to exit
        if key == ord("q"):
            break
        elif count == 50:
            break

    # Release memory
    video.release()


name = str(input("Type your name: "))
storeUserImage(name)
=======

        # Press 'q' to exit
        if key == ord("q") or count == 65:
            break
    print('added!')
    # Release memory
    video.release()

storeUserImage()
>>>>>>> Merge
cv2.destroyAllWindows()
