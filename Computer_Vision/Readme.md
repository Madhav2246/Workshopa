# Computer Vision using YOLO

### Presentation link: https://my.visme.co/view/n0epem7m-advancements-in-yolo-and-object-detection

### Note: to add custom data use your own files and for video detection use your file
## Introduction
This project uses the YOLOv10 model to perform object detection on a video stream. The model is trained on the COCO dataset and can detect 80 different classes of objects.

### Requirements
Python 3.8+\
ultralytics\
OpenCV\
cvzone\
math

### Installation
To install the required libraries, run the following command:

### #bash
pip install ultralytics opencv-python cvzone

### Code Explanation
The code uses the YOLOv10 model to detect objects in a video stream. Here's a brief explanation of the code:

The script starts by importing the required libraries and loading the YOLOv10 model.\
The video stream is captured using OpenCV and resized to a smaller resolution for faster processing.\
The model function is used to detect objects in the video stream, and the results are stored in the results variable.\
The script then loops through the detected objects and draws bounding boxes around them using cvzone.\
The class name and confidence score are displayed on top of the bounding box using cvzone.putTextRect.\
Finally, the output is displayed using cv2.imshow.

### Example Use Cases
Object detection in surveillance videos\
Autonomous vehicles\
Robotics\
Image classification
