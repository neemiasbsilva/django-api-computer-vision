from django.conf import settings
import numpy as np
import cv2


def crop_image(path, x, y, dx, dy):
    # cv2.imwrite(filename='croped_img.jpg', img=frame)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if type(img) is np.ndarray:

        img = cv2.resize(img, (512, 512))

        img_rectangle = img[y: y + dy, x: x + dx]

        cv2.imwrite(path, img_rectangle)
    else:
        print("Error!!!")
        print(img)