"""
This function will open webcam and start capture front_face's user
"""
import cv2
import os
import time


def storeUserImage(name):
    face_cascade = cv2.CascadeClassifier(
        "./cascades/data/haarcascade_frontalface_alt.xml"
    )
    video = cv2.VideoCapture(0)
    count = 0
    # creater new directory in user_capture
    os.makedirs("./images/" + str(name))
    while True:
        check, data = video.read()
        faces = face_cascade.detectMultiScale(data, scaleFactor=1.5, minNeighbors=5)
        for x, y, w, h in faces:
            # if count % 10 == 0:
            cv2.rectangle(data, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imwrite("./images/" + str(name) + "/" + str(count) + ".jpg", data)
            count += 1
        cv2.waitKey(3)
        cv2.imshow("Face Detect", data)
        key = cv2.waitKey(1)
        # Press 'q' to exit
        if key == ord("q"):
            break
        elif count == 50:
            break

    # Release memory
    video.release()


name = str(input("Type your name: "))
storeUserImage(name)
cv2.destroyAllWindows()
