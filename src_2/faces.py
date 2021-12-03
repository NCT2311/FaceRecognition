import numpy as np
import cv2
import pickle
from modules import *

face_cascade = cv2.CascadeClassifier("./cascades/data/haarcascade_frontalface_alt2.xml")
eye_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_smile.xml")

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


count = 50
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
        if conf >= 45:  # and conf <= 85:
            print(id_)
            # print(labels[id_])

            if temp_id != id_:
                count = 50
            temp_id = id_
            person_name = labels[id_]
            count = count - 1

            # if temp_id == id_:
            #     count = count - 1
            # temp_id = id_
            # person_name = labels[id_]

            if count == 0:
                flag = 1
                break

            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

        # Draw a Rectangle
        color = (255, 0, 0)  # BGR 0 - 255
        stroke = 2
        end_cord_x = x + w  # Width of Rectangle
        end_cord_y = y + h  # Height of Recctangle
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    # Display the resulting frame
    cv2.imshow("frame", frame)
    if flag == 1:
        print("Successfully")
        print(person_name)
        # Create last photo into folder
        img_item = (
            "../public/img/"
            + person_name
            + str(datetime.now().strftime("%Y%m%d%H%M%S"))
            + ".png"
        )
        print(img_item)
        cv2.imwrite(img_item, frame)
        collection = Excute()
        collection.addTurn(getImageUrl(), False, person_name, 0, True)
        sendMail("http://localhost:3000/home")
        break
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
