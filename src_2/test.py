import cv2
import os
import numpy as np
from PIL import Image
import pickle

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

make_720p()

def detect(name):
    directory = ".\\data\\{}".format(name)
    for filename in os.listdir(directory):
        frame = cv2.imread(os.path.join(directory, filename), cv2.IMREAD_COLOR)
        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Cascade face_cascade
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y : y + h, x : x + w]  # (y_coordinate_start, y_coordinate_end)
            id_, conf = recognizer.predict(roi_gray)
            if conf >= 50:
                name = labels[id_]
                if name != '':
                    return name
        
    return 'cannot found'

def iterativeDataSet(name):
    '''compare name with another'''
    count = 0
    folderPath = ".\\data"
    for folderName in os.listdir(folderPath):
        personName = detect(folderName)
        print(personName)
        if personName == name and personName == folderName:
            count += 1
        elif personName != name and personName != 'cannot found':
            count += 1
    print("Accurate: {:.0f}%".format(100*count/len(os.listdir(folderPath))))

training()
# print(detect('61aa3105223797e0e7ad043b'))
iterativeDataSet('congthanh')

cap.release()
cv2.destroyAllWindows()

'''Plotting'''

def plot():  
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array([0,1,2,3])
    y = np.array([5,3,2,4])

    plt.plot(x, y)
    plt.xlabel('Number of image use for training/person')
    plt.ylabel('Accurate')
    plt.show()

# plot()

