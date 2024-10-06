from ultralytics import YOLO
import cv2
 
model = YOLO("yolo-weights/yolov8s.pt")
print(model)
results = model("traffic.jpg" , show=True)
cv2.waitKey(0)
