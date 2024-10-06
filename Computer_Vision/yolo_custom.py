from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='dataset/data.yaml',
   imgsz=1280,
   epochs=5,
   batch=8,
   name='custom_yolov8')