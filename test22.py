import cv2
import random

img = cv2.imread('assets/damas.jpg', -1)
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)

tag = img[500:700, 600:900]
img[100:300, 650:950] = tag


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
