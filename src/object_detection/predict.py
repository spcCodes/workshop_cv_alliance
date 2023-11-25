from ultralytics import YOLO
from PIL import Image
import os , glob
from tqdm import tqdm

image_output = "data/test_output_od"
if not os.path.exists(image_output):
    os.makedirs(image_output)

#loading the model
print("Loading the model!")
model = YOLO("models/best.pt")
print("Model Loaded!")

image_path = "data/object_Detection/hard_workers/test/images/006984_jpg.rf.709c61978da32a98e9b0a447f76465d8.jpg"
image_name = image_path.split("/")[-1]
result = model.predict(image_path)[0]
result_image = result.plot(line_width=1)
result_image = result_image[:, :, ::-1]
result_image = Image.fromarray(result_image)
result_image.save(os.path.join(image_output, image_name))








# print(type(result_image))
# print("*********************************************")
# result_bbox = result.boxes.xywhn.tolist()
# print(result_bbox)
# print("*********************************************")
# print(result.boxes)
