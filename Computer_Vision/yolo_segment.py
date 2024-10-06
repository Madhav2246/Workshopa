from ultralytics import YOLO
import cv2
 
model = YOLO("yolo-weights/yolov8l-seg.pt")
 
results = model("traffic.jpg" , show=True)
cv2.waitKey(0)
