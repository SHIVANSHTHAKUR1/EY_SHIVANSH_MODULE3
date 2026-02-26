import cv2
import numpy as np

#create a blank white image(canvas)
canvas= np.ones((400, 400, 3), dtype=np.uint8) # *255 is used to make the canvas white, as np.ones creates a black canvas by default

cv2.line(canvas, (0, 0), (400, 400), (255, 0, 0), thickness=5) #blue line diagonal (x1,y1) to (x2,y2)
cv2.line(canvas, (50, 100), (350, 100), (0, 255, 0), thickness=5) #green line
cv2.rectangle(canvas, (50, 150), (350, 300), (0, 0, 255), thickness=5) #red (rectangle top left corner to bottom right corner)
#show the canvas
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)  
cv2.destroyAllWindows()