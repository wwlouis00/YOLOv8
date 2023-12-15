from ultralytics import YOLO

model = YOLO("model/yolov8n.pt")

# realtime camera
model.predict(0,show=True,conf=0.4)
