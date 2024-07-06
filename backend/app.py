from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

model = load_model('app/model/model.h5')

def preprocess_image(image):
    image = cv2.resize(image, (48, 48))
    image = image / 255.0
    image = image.reshape(1, 48, 48, 1)
    return image

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    emotion = np.argmax(prediction)
    emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    return jsonify({'emotion': emotions[emotion]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
