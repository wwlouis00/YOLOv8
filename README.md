# YOLOv8 簡介

YOLOv8（You Only Look Once Version 8）是目標檢測的深度學習模型，它是 YOLO（You Only Look Once）系列的最新版本。YOLOv8 通過一次前向傳播即可在圖像中同時檢測多個物體，並為每個物體提供其邊界框和類別標籤。

## 主要特點

- **即時目標檢測**：YOLOv8 是一個即時目標檢測模型，它可以在一次前向傳播中同時識別圖像中的多個物體。這使它在需要高效處理的應用中非常有用。

- **多尺度檢測**：YOLOv8 通過使用不同尺度的特徵圖來檢測不同大小的物體，這使得它能夠處理各種大小的物體，從而提高檢測的準確性。

- **強大的後處理**：YOLOv8 使用了一系列的後處理技術，包括非極大值抑制（NMS）和閾值過濾，來消除重疊的檢測框和過濾低置信度的檢測。

- **支持多種數據集**：YOLOv8 可以用於不同類型的數據集，並且可以進行細微的調整以適應不同的應用場景。

## 使用場景

- **物體檢測**：YOLOv8 常用於物體檢測任務，如交通監控、人臉識別、工業檢測等。

- **自動駕駛**：YOLOv8 可用於自動駕駛中的物體和行人檢測，幫助車輛識別周圍的障礙物。

- **安防監控**：YOLOv8 可用於安防監控中，幫助監測人流、車輛和其他物體。

## 學習資源

您可以通過研讀 YOLOv8 的相關論文、查看開源代碼庫和參加深度學習相關的線上課程來深入了解 YOLOv8 的運作原理和使用方法。

## 使用 Python 與 Ultralytics

[Ultralytics](https://www.ultralytics.com/) 是一個開源的深度學習研究框架，旨在提供易於使用的工具，協助開發者進行目標檢測、圖像分類和語意分割等任務。這裡提供了一個簡單的介紹和使用 Ultralytics 的方法：

## 安裝 Ultralytics

首先，你需要使用 pip 安裝 Ultralytics 模組。打開終端機並執行以下命令：

```
pip install -U ultralytics
```

## 使用目標檢測模型

Ultralytics 提供了一個名為 [YOLOv5](https://github.com/ultralytics/yolov5) 的目標檢測模型。以下是一個簡單的範例，展示了如何使用 YOLOv5 模型進行目標檢測：

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

這個範例示範了使用 YOLOv5 模型進行目標檢測的基本步驟，包括初始化模型、載入圖像、執行目標檢測，並將預測結果顯示在圖像上。

透過 Ultralytics 的工具，開發者可以更方便地進行目標檢測任務，並根據需要進行模型調整和結果視覺化。

