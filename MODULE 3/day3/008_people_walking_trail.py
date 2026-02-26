import cv2

from ultralytics import YOLO

from collections import defaultdict, deque

model = YOLO('yolov8n.pt')
video_path = r'vid\WhatsApp Video 2026-02-25 at 3.03.46 PM.mp4'

capture = cv2.VideoCapture(video_path)
id_map = {}
next_id = 0
appearance_count = defaultdict(int)
trail = defaultdict(lambda: deque(maxlen=30))  # Store the last 30 positions for each object

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Use the tracker API so YOLO keeps IDs between frames.
    res = model.track(frame, classes=[0], tracker='bytetrack.yaml', persist=True, verbose=False)
    annotated_frame = res[0].plot()

    if res[0].boxes.id is None:
        cv2.imshow("People Walking Trail", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    boxes = res[0].boxes.xyxy.cpu().numpy()
    ids = res[0].boxes.id.cpu().numpy()

    for box, obj_id in zip(boxes, ids):
        x1, y1, x2, y2 = box.astype(int)
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2

        appearance_count[obj_id] += 1

        if appearance_count[obj_id] > 5 and obj_id not in id_map:
            id_map[obj_id] = next_id
            next_id += 1

        person_id = id_map.get(obj_id, obj_id)
        trail[person_id].append((center_x, center_y))

        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            annotated_frame,
            f"Person {person_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv2.LINE_AA
        )

        for i in range(1, len(trail[person_id])):
            cv2.line(
                annotated_frame,
                trail[person_id][i - 1],
                trail[person_id][i],
                (0, 0, 255),
                2
            )

    cv2.imshow("People Walking Trail", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()