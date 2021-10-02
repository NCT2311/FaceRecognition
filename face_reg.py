# import opencv
import cv2
import os

def storeUserImage(name):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    video = cv2.VideoCapture(0)
    count = 0
    os.makedirs('user_capture/' + str(name))
    while True:
        check, data = video.read()
        faces = face_cascade.detectMultiScale(data)
        for x,y,w,h in faces:
            
            cv2.rectangle(data, (x,y), (x+w,y+h), (0,255,0), 3)
            cv2.imwrite('user_capture/' + str(name) + '/' + '.' + str(count) + '.jpg', data)
            count += 1
        
        cv2.waitKey(3)
        cv2.imshow('Face Detect', data)
        key = cv2.waitKey(1)
        # Press 'q' to exit
        if key == ord('q'):
            break
        elif count == 10:
            break
    # Release memory
    video.release()
cv2.destroyAllWindows()

