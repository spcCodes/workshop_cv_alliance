from ultralytics import YOLO

model = YOLO("yolov8m.pt")

#train the model
model.train(
    data = "/content/drive/MyDrive/alliance_university/object_detection/data.yaml",
    epochs = 5,
    imgsz = (640,640),
    batch = 4,
    optimizer = "Adam",
    lr0=1e-3
)