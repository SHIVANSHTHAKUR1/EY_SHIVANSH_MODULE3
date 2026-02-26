import cv2

#read
image = cv2.imread('img\IMG20210110174853.jpg')


#resize
resized_image = cv2.resize(image, (400, 400))
#convert image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#convert to blur image
blur_image = cv2.GaussianBlur(gray_image, (5,5), 0)
#edges to blur image 
edges = cv2.Canny(blur_image, 100, 200)

#display
# cv2.imshow('img\resized_cat.jpg', resized_image)
# cv2.imshow('img\original_cat.jpg', image)
# cv2.imshow('img\gray_cat.jpg', gray_image)
# cv2.imshow('img\blur_cat.jpg', blur_image)
cv2.imshow('img\edges_cat.jpg', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
