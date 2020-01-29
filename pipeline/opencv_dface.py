from django.conf import settings
import numpy as np
import matplotlib.pyplot as plt
import cv2

def opencv_dface(path):

    img = cv2.imread(path)

    if type(img) is np.ndarray:
        img_temp = img.copy()
        baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL

        face_cascade = cv2.CascadeClassifier(baseUrl+'haarcascade_frontalface_default.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # region of interest
            roi_gray = gray[y: y+h, x: x+w]
            roi_color = img[y: y+h, x: x+w]

        print(img == img_temp)
        plt.imshow(img)
        cv2.imwrite(path, img)

    else:
        print("Error!")
        print(path)