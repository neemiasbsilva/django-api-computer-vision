import cv2
import numpy as np

def binarize_mask(path, r, g, b, k):
    img = cv2.imread(path)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(img[:,:,0])
    img_b = img[:, :, 0] * r + img[:, :, 1] * g + img[:, :, 2] * b
    img_b = img_b > k
    img_b = np.uint8(img_b)
    img_b *= 255

    cv2.imwrite(path, img_b)