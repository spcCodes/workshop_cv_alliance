from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import io
import numpy as np
from PIL import Image
from fastai.vision.all import load_learner

# Define Pydantic models for request and response
class ImageRequest(BaseModel):
    file: bytes

class Prediction(BaseModel):
    class_name: str
    probability: float

# Load your Fastai model
model_path = 'models/bears_model.pkl'
learner = load_learner(model_path)

# Define FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to bear prediction service"}

# Helper function to preprocess the image
def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224))  # Resize according to your model's requirements
    img_tensor = np.array(img)
    img_tensor = Image.fromarray(img_tensor).convert("RGB")  # Convert to RGB if needed
    return img_tensor

# Endpoint to predict jusing bytes
@app.post("/predict", response_model=Prediction)
async def predict_image(image: ImageRequest):
    img_tensor = preprocess_image(image.file)
    prediction, _, probs = learner.predict(img_tensor)
    class_name = str(prediction)
    probability = float(probs[np.argmax(probs)])
    probability = f"{probability:.4f}"
    return {"class_name": class_name, "probability": probability}

# Endpoint to accept image file upload and make a prediction
@app.post("/predict_upload", response_model=Prediction)
async def predict_from_upload(file: UploadFile = File(...)):
    contents = await file.read()
    img_tensor = preprocess_image(contents)
    prediction, _, probs = learner.predict(img_tensor)
    class_name = str(prediction)
    probability = float(probs[np.argmax(probs)])
    probability = f"{probability:.4f}"
    return {"class_name": class_name, "probability": probability}




#uvicorn src.app:app --reload