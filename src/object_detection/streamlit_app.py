import streamlit as st
from PIL import Image as PILImage
import io
from ultralytics import YOLO
import os
import numpy as np
from PIL import Image

# Loading the YOLO model
@st.cache(allow_output_mutation=True)
def load_model():
    return YOLO("models/best.pt")

st.title("Workers Safety Detection")

# Load the model
model = load_model()

# Sidebar to upload an image
source_image = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2)

with col1:
    if source_image:
            uploaded_image = Image.open(source_image)
            # adding the uploaded image to the page with caption
            st.image(
                image=source_image,
                caption="Uploaded Image",
                use_column_width=True
            )

if source_image:
    if st.button("Predict"):
        with st.spinner("Running..."):
            res = model.predict(uploaded_image)
            boxes = res[0].boxes
            res_plotted = res[0].plot()[:, :, ::-1]

            with col2:
                    st.image(res_plotted,
                             caption="Detected Image",
                             use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write(box.xywh)
                    except Exception as ex:
                        st.write("No image is uploaded yet!")
                        st.write(ex)
