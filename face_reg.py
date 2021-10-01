# import opencv
import cv2
import sqlite3

# def insertUsers2DB():
#     pass

# Using library facedetect written by opencv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Open webcam
video = cv2.VideoCapture(0)
# Main
while True:
    # Read data from webcam
    check, data = video.read()
    # Detect data
    faces = face_cascade.detectMultiScale(data)
    for x,y,w,h in faces:
        # Draw rect around faces
        frame = cv2.rectangle(data, (x,y), (x+w,y+h), (0,255,0), 3)
    # Show the console
    cv2.imshow('Face Detect', data)
    key = cv2.waitKey(1)
    # Press 'q' to exit
    if key == ord('q'):
        break
# Release memory
video.release()
cv2.destroyAllWindows()