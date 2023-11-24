import os
from fastai.vision.all import *
import io
import numpy as np
from PIL import Image
from fastai.vision.all import vision_learner , load_learner

class_names = ['brown', 'grizzly', 'black']
model_path = 'models/bears_model.pkl' 
learner = load_learner(model_path)

def predict_image(image_path):
    image = PILImage.create(image_path)
    prediction, a, probs = learner.predict(image)
    class_name = str(prediction)
    probability = float(probs[np.argmax(probs)])
    probability = f"{probability:.4f}"
    return {"class_name": class_name, "probability": probability}

if __name__ == '__main__':
    image_path = 'data/bears/black/1cc00f52-4aa6-413b-b794-b575ffc1b8a4.jpg'
    prediction = predict_image(image_path)
    print(prediction)


#python src/predict.py