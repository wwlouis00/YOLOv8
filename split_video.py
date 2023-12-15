# Splitting a Video into Images
import cv2 as cv

# Open the video file
video_path = 'your video'  # Replace with the path to your video file

cap = cv.VideoCapture(video_path)

# Ensure the video file is successfully opened
if not cap.isOpened():
    print("Unable to open the video file")
    exit()

frame_count = 0

while True:
    # Read a frame
    ret, frame = cap.read()
    # If the video ends, exit the loop
    if not ret:
        break
    # Save the current frame as an image file
    output_file = f"video/frame_{frame_count}.jpg"  # Save each frame as a separate image file
    cv.imwrite(output_file, frame)
    
    frame_count += 1

# Release the video file
cap.release()

print(f"Total frames split: {frame_count}")
