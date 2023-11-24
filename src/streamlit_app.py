import streamlit as st
import requests
from PIL import Image
import io

# Define your FastAPI server URL
FASTAPI_URL = 'http://localhost:8000'  # Replace with your FastAPI server URL

# Streamlit app layout
st.title("Bear Prediction App")

# Image upload at the top of the app
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png"])

# Function to make prediction using FastAPI endpoint
def predict_image(file):
    endpoint = f"{FASTAPI_URL}/predict_upload"
    response = requests.post(endpoint, files={"file": file})
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Display predictions and resized image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Display uploaded image in a smaller size on the left side
    st.image(image, caption='Uploaded Image', width=256)

    # Prediction button
    if st.button('Predict'):
        # Resize the image
        resized_image = image.resize((224, 224))
        resized_img_bytes = io.BytesIO()
        resized_image.save(resized_img_bytes, format='JPEG')
        resized_img_bytes.seek(0)  # Go back to the start of the buffer
        resized_img_bytes = resized_img_bytes.read()

        # Make prediction
        prediction = predict_image(resized_img_bytes)
        if prediction:
            st.subheader("Results:")
            st.write(f"Class: {prediction['class_name']}")
            st.write(f"Probability: {prediction['probability']}")

# Error handling if no image is uploaded
else:
    st.warning("Please upload an image to make predictions.")


#streamlit run src/streamlit_app.py