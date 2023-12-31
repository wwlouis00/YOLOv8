from ultralytics import YOLO
import glob
from IPython.display import Image, display

# Loading your model.
model = YOLO("your_model.pt")
model.info()

# predict your image or video
# If you want to capture real-time camera images, please change the "source" to "0" or "1."
results = model.predict(source="your_image",project="result/your_save_dir",name="your_folder_name",save=True)
print(results)

# Detecting images(.jpg or .png) in an entire folder.
for image_path in glob.glob(f'your_image/*jpg'):
      results = model.predict(source=image_path,project="result/your_save_dir",name="your_folder_name",save=True)
      print("\n")
