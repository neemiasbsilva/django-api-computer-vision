import cv2
import numpy as np


def subtract(path_oimg, path_img):

    oimg = cv2.imread(path_oimg)
    img = cv2.imread(path_img)
    oimg = cv2.resize(oimg, (512, 512))
    img = cv2.resize(img, (512, 512))
    img_sub = cv2.subtract(oimg, img)

    cv2.imwrite(path_oimg, img_sub)