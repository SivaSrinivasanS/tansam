# Import necessary libraries
# import streamlit as st
# from PIL import Image, ImageOps
# import requests
# import numpy as np
#
# st.write("""
#          # Image Classification App
#          """
#          )
#
# file = st.file_uploader("Please upload an image", type=["jpg", "png"])
#
# def import_and_predict(image_data):
#
#     # Preprocess the image
#     size = (256, 256)  # Resize the image to the size your model expects
#     image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
#     image = np.asarray(image)
#     img = np.expand_dims(image, 0)  # Expand dimensions to fit model input
#
#     # Make prediction by sending a request to the FastAPI server
#     response = requests.post("http://localhost:8000/predict", files={"file": img.tobytes()})
#
#     return response.json()
#
# if file is None:
#     st.text("Please upload an image file")
# else:
#     image = Image.open(file)
#     st.image(image, use_column_width=True)
#     predictions = import_and_predict(image)


# Import necessary libraries
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import tensorflow as tf
import numpy as np

# Initialize FastAPI app and CORS middleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = tf.keras.models.load_model('C:/DLModel/1')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read the image file and convert it to a NumPy array
    image = np.frombuffer(await file.read(), dtype=np.uint8)

    # Preprocess the image
    img = tf.image.convert_image_dtype(image, tf.float32)

    # Make prediction
    prediction = model.predict(img)

    return prediction

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
