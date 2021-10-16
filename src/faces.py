import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    './cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Cascade face_cascade
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)
    for(x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]  # (y_coordinate_start, y_coordinate_end)
        roi_color = frame[y:y+h, x:x+w]
		# Recognize: Deep learned model predict keras tensorflow pytorch scikit learn
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)
        # Draw a Rectangle
        color = (255, 0, 0)  # BGR 0 - 255
        stroke = 2
        end_cord_x = x + w  # Width of Rectangle
        end_cord_y = y + h  # Height of Recctangle
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
