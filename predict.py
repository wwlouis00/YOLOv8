from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import glob
from IPython.display import Image, display

# Loading your model.
model = YOLO("your_model.pt")
model.info()

# predict your image or video
results = model.predict(source="your_image",project="your_save_dir",name="your_folder_name",save=True)
print(results)

# Detecting images(.jpg or .png) in an entire folder.
for image_path in glob.glob(f'your_image/*jpg'):
      results = model.predict(source=image_path,project="your_save_dir",name="your_folder_name",save=True)
      print("\n")
