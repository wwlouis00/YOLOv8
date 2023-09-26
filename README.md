# YOLOv8 簡介

YOLOv8 (You Only Look Once Version 8) is a deep learning model for object detection, and it represents the latest iteration in the YOLO (You Only Look Once) series. YOLOv8 is capable of simultaneously detecting multiple objects within an image in a single forward pass and provides bounding boxes and class labels for each detected object.

## 主要特點

- **Real-time Object Detection**: YOLOv8 is a real-time object detection model capable of simultaneously identifying multiple objects in an image in a single forward pass. This makes it highly useful for applications requiring efficient processing.

- **Multi-scale Detection**: YOLOv8 employs different-scale feature maps to detect objects of varying sizes, enhancing its ability to handle objects of various dimensions and improving detection accuracy.
 
- **Robust Post-processing**: YOLOv8 utilizes a series of post-processing techniques, including Non-Maximum Suppression (NMS) and threshold filtering, to eliminate overlapping detection boxes and filter out detections with low confidence scores.

- **Support for Multiple Datasets**: YOLOv8 can be applied to various types of datasets and can be fine-tuned to adapt to different application scenarios.

## 使用場景

- **Object Detection**: YOLOv8 is commonly used for object detection tasks such as traffic monitoring, facial recognition, industrial inspection, and more.

- **Autonomous Driving**: YOLOv8 can be applied to object and pedestrian detection in autonomous driving, assisting vehicles in identifying obstacles in their surroundings.

- **Security Surveillance**: YOLOv8 finds applications in security surveillance, helping monitor human traffic, vehicles, and other objects.

## 學習資源

You can gain a deeper understanding of how YOLOv8 works and how to use it by studying related research papers, exploring open-source code repositories, and participating in online courses related to deep learning.

## 使用 Python 與 Ultralytics

[Ultralytics](https://www.ultralytics.com/) 是一個開源的深度學習研究框架，旨在提供易於使用的工具，協助開發者進行目標檢測、圖像分類和語意分割等任務。這裡提供了一個簡單的介紹和使用 Ultralytics 的方法：

## 安裝 Ultralytics

首先，你需要使用 pip 安裝 Ultralytics 模組。打開終端機並執行以下命令：

```
pip install -U ultralytics
```

## 使用目標檢測模型

Ultralytics is an open-source deep learning research framework designed to offer user-friendly tools for developers working on tasks like object detection, image classification, and semantic segmentation. Here is a brief introduction and guide on how to use Ultralytics.

```python
import torch
from PIL import Image
from pathlib import Path
from matplotlib import pyplot as plt
from IPython.display import display

# 匯入目標檢測模型
from yolov5 import YOLOv5

# 初始化模型
model = YOLOv5()

# 載入圖像
image_path = Path("path/to/your/image.jpg")
image = Image.open(image_path)

# 執行目標檢測
results = model(image)

# 取得預測結果
predictions = results.pandas().xyxy[0]

# 顯示圖像和預測框
plt.imshow(image)
plt.axis('off')

# 繪製預測框
for _, prediction in predictions.iterrows():
    xmin, ymin, xmax, ymax = prediction[["xmin", "ymin", "xmax", "ymax"]]
    plt.rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, color="red")
    plt.text(xmin, ymin, prediction["name"], color="red")

# 顯示圖像和預測結果
plt.show()
```
This example demonstrates the basic steps of performing object detection using the YOLOv5 model, including initializing the model, loading an image, executing object detection, and displaying the prediction results on the image.
With the tools provided by Ultralytics, developers can conduct object detection tasks more conveniently and make model adjustments and result visualizations as needed.

