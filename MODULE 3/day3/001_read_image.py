import cv2 

image = cv2.imread('img\Cat03.jpg')

cv2.imshow('cat', image)

cv2.waitKey(0)
cv2.destroyAllWindows()