from django.conf import settings
import numpy as np
import cv2


def crop_image(path, x, y, dx, dy):
    # cv2.imwrite(filename='croped_img.jpg', img=frame)
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if type(img) is np.ndarray:

        # img = cv2.resize(img, (512, 512))
        x = max(0, x)
        y = max(0, y)

        x = min(x, img.shape[1])
        y = min(y, img.shape[0])

        x2 = min(dx + x, img.shape[1])
        y2 = min(y + dy, img.shape[0])

        img_rectangle = img[y: y2, x: x2]

        cv2.imwrite(path, img_rectangle)
    else:
        print("Error!!!")
        print(img)