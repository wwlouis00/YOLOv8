from ultralytics import YOLO

model = YOLO("model/yolov8n-seg.pt")

model.predict("/home/wwlouis/project/yolov8/datasets/images/church.JPG",show=True,conf=0.4,project="/home/wwlouis/project/yolov8/result/segment",save=True)
