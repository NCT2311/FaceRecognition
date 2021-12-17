import numpy as np
import cv2
import pickle
from modules import *
import pymongo

face_cascade = cv2.CascadeClassifier("./cascades/data/haarcascade_frontalface_alt2.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0)

# Rescale frame
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)


count_stranger = 40
count_relative = 30
temp_id = 0
flag = 0
person_name = ""

make_720p()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Cascade face_cascade
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        # print(x, y, w, h)
        roi_gray = gray[y : y + h, x : x + w]  # (y_coordinate_start, y_coordinate_end)
        roi_color = frame[y : y + h, x : x + w]
        # Recognize: Deep learned model predict keras tensorflow pytorch scikit learn
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45 and conf <= 85:
            # count_relative to recognize
            if temp_id != id_:
                count_relative = 30
            temp_id = id_
            person_name = labels[id_]
            count_relative = count_relative - 1

            # # Write person's name
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # name = labels[id_]
            # color = (255, 255, 255)
            # stroke = 2
            # cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            if count_relative == 0:
                print("Successfully")
                count_stranger = 40
                count_relative = 30
                flag = 1
                break
        else:
            # Write person's name
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # name = "Unknown"
            # color = (255, 255, 255)
            # stroke = 2
            # cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            count_stranger = count_stranger - 1
            if count_stranger == 0:
                print("Who are you??")
                count_stranger = 40
                count_relative = 30
                flag = 2
                break
        # # Draw a Rectangle
        color = (255, 0, 0)  # BGR 0 - 255
        stroke = 2
        end_cord_x = x + w  # Width of Rectangle
        end_cord_y = y + h  # Height of Recctangle
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # Display the resulting frame
    cv2.imshow("frame", frame)
    if flag == 1:
        flag = 0
        # Nguoi quen
        # Create last photo into folder
        img_item = (
            "../public/img/"
            + person_name
            + str(datetime.now().strftime("%Y%m%d%H%M%S"))
            + ".png"
        )
        cv2.imwrite(img_item, frame)
        # # Insert turn of nguoi quen
        Fname, Lname = Mongo.getNameById("", person_name)
        imgUrl = Control.getImageUrl("")
        Control.addTurn("", imgUrl, person_name, 0, True, True)
        # break
    if flag == 2:
        flag = 0
        # Nguoi laa
        Control.addPerson("", "undefined", "undefined", False)
        id = persons.find().sort("_id", pymongo.DESCENDING).limit(1)[0]["_id"]
        img_item = (
            "../public/img/"
            + str(id)
            + str(datetime.now().strftime("%Y%m%d%H%M%S"))
            + ".png"
        )
        cv2.imwrite(img_item, frame)
        imgUrl = Control.getImageUrl("")
        Control.addTurn("", imgUrl, id, 0, False, False)
        turnId = turns.find().sort("_id", pymongo.DESCENDING).limit(1)[0]["_id"]
        Mongo.updateFlag("")
        getResponse(str(turnId))
        sendMail()
        # break
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
