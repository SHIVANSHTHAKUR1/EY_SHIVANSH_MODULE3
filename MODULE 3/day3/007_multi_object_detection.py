import cv2
from ultralytics import YOLO
model = YOLO('yolov8n.pt')

#read fromm video file
video_path ='vid\WhatsApp Video 2026-02-25 at 2.40.16 PM.mp4'
cap = cv2.VideoCapture(video_path)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame) #yoou can add classes to detect by passing a list of class ids to the model, for example: results = model(frame, classes=[0, 1, 2]) to detect only person, bicycle and car
    #classes in yolo format: 0=person, 1=bicycle, 2=car, 3=motorcycle, 4=airplane, 5=bus, 6=train, 7=truck, 8=boat, 9=traffic light
    annotated_frame = results[0].plot()
    cv2.imshow('Multi Object Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()