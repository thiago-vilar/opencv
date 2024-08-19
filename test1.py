import cv2

img = cv2.imread('assets\damas.jpg', 0)
img = cv2.resize(img,(0,0), fx=0.2, fy=0.2)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_img.jpg', img)

cv2.imshow('assets\Image ', img)
cv2.waitKey(0)
cv2. destroyAllWindows()
