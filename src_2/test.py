import cv2
import os
import numpy as np
from PIL import Image
import pickle
from time import sleep

def training():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "data")

    face_cascade = cv2.CascadeClassifier("./cascades/data/haarcascade_frontalface_alt2.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = (os.path.basename(root).replace(" ", "-").lower())  # os.path.dirname(path) == root
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]

                pil_image = Image.open(path).convert("L")  # grayscale
                size = (550, 550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image, "uint8")
                # print(image_array)
                faces = face_cascade.detectMultiScale(
                    image_array, scaleFactor=1.5, minNeighbors=5
                )
                for (x, y, w, h) in faces:
                    roi = image_array[y : y + h, x : x + w]
                    x_train.append(roi)
                    y_labels.append(id_)

    with open("labels.pickle", "wb") as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainner.yml")

    print('Traning done.')

# training()
###############################################################################################################
###############################################################################################################
###############################################################################################################

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

temp_id = 0
flag = 0
person_name1, person_name2 = "", ""
make_720p()

n = 50
run = True

# 'src_2\data\congthanh\0.jpg'
# img = cv2.imread("src_2\data\congthanh\0.jpg")
# cv2.imshow("img", img)
# sleep(5)

def person1(name):
    Path = ".\\data\\{}".format(name)
    for filename in os.listdir(Path):
        print(".\\data\\{}\\{}".format(name, filename))
        img = cv2.imread(".\data\{}\{}".format(name, filename), cv2.IMREAD_COLOR)
        frame = img
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Cascade face_cascade
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:    
            roi_gray = gray[y : y + h, x : x + w]  # (y_coordinate_start, y_coordinate_end)
            roi_color = frame[y : y + h, x : x + w]
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45:
                temp_id = id_
                person_name1 = labels[id_]
                # if person_name1 != '':
                #     return person_name1
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            color = (255, 0, 0)  # BGR 0 - 255
            stroke = 2
            end_cord_x = x + w  # Width of Rectangle
            end_cord_y = y + h  # Height of Recctangle
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        cv2.imshow("frame", frame)
        sleep(1)
    return 'cannot found'

# person1('congthanh')

def person2(name):
    for index in range(n):
        img = cv2.imread(".\\images\\{}\\{}.jpg".format(name, index), cv2.IMREAD_COLOR)
        frame = img
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Cascade face_cascade
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:    
            roi_gray = gray[y : y + h, x : x + w]  # (y_coordinate_start, y_coordinate_end)
            roi_color = frame[y : y + h, x : x + w]
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 45:
                temp_id = id_
                person_name2 = labels[id_]
                # if person_name2 != '':
                #     return person_name2
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            color = (255, 0, 0)  # BGR 0 - 255
            stroke = 2
            end_cord_x = x + w  # Width of Rectangle
            end_cord_y = y + h  # Height of Recctangle
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        cv2.imshow("img", img)
    return 'cannot found'
person2('congthanh')

def iterativeDataSet(name):
    '''compare name with another'''
    # path = ".\\data\\{}".format(name)
    folderPath = ".\\data"
    for folderName in os.listdir(folderPath):
        childPath = ".\\data\\{}".format(folderName)
        for filename in os.listdir(childPath):
            person1(str(filename))
        # print(os.path.join(directory, filename))
    # img = cv2.imread(".\\images\\{}\\*.jpg".format(name, index), cv2.IMREAD_COLOR)

# iterativeDataSet('congthanh')

# print("person1: {0}\nperson2: {1}\nResult: {2}".format(
#     person1('61a4ededdd2f672c6d602ef6'), 
#     person2('congthanh'),
#     person1('61a4ededdd2f672c6d602ef6') != person2('congthanh')))

cap.release()
cv2.destroyAllWindows()
