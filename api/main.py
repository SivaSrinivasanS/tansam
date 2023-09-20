#
#
# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
#
# app = FastAPI()
#
# origins = [
#     "*",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# MODEL = tf.keras.models.load_model("C:/DLModel/1")
#
#
# CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
#
# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"
#
# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image
#
# @app.post("/predict")
# async def predict(
#     file: UploadFile = File(...)
# ):
#     image = read_file_as_image(await file.read())
#     img_batch = np.expand_dims(image, 0)
#
#     predictions = MODEL.predict(img_batch)
#
#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = np.max(predictions[0])
#     return {
#         'class': predicted_class,
#         'confidence': float(confidence)
#     }
#
# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)
#

# from fastapi import FastAPI, File, UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
# import numpy as np
# from io import BytesIO
# from PIL import Image
# import tensorflow as tf
#
# app = FastAPI()
#
# origins = [
#     "http://localhost:3000",  # Replace with your frontend URL
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# MODEL = tf.keras.models.load_model("C:/DLModel/1")
# CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]
#
# @app.get("/ping")
# async def ping():
#     return "Hello, I am alive"
#
# def read_file_as_image(data) -> np.ndarray:
#     image = np.array(Image.open(BytesIO(data)))
#     return image
#
# @app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image = read_file_as_image(await file.read())
#     img_batch = np.expand_dims(image, 0)
#
#     predictions = MODEL.predict(img_batch)
#
#     predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
#     confidence = float(np.max(predictions[0]))
#
#     return {
#         'class': predicted_class,
#         'confidence': confidence
#     }
#
# if __name__ == "__main__":
#     uvicorn.run(app, host='localhost', port=8000)

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost:3000",  # Replace with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("C:/DLModel/1")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)

        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))

        return JSONResponse(content={
            'class': predicted_class,
            'confidence': confidence
        })

    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)

