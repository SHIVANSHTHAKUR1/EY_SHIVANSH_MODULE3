import cv2 
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Load the image
img = cv2.imread("img\Screenshot 2024-01-19 001429.png")
results = model(img)
# annotate the image
annotated_img = results[0].plot()
# Display the annotated image
cv2.imshow("Annotated Image", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()