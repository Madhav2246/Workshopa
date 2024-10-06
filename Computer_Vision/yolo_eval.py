from ultralytics import YOLO
model = YOLO('runs/train/custom_yolov8/weights/best.pt')  # Path to the best-trained weights

# Evaluate the model
metrics = model.val()

# Test the model on new images
results = model.predict(source='path/to/test_image.jpg', show=True)
