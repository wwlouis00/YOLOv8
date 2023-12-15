from ultralytics import YOLO                                                                                                                                                              2 # from ultralytics.yolo.v8.detect.predict import DetectionPredictor

model = YOLO("model/yolov8m-seg.pt")
result = model.predict(source='0',show=True)
# result = model.predict(source="image or video",project="your save dir",name="file name",show=True,save=True)
print(result)
