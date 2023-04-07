import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import model_from_json
import cv2 as cv

def is_winnie_the_pooh():
    json_file = open('app/models/xi.json')
    loaded_model_json = json_file.read()
    json_file.close()

    model = model_from_json(loaded_model_json)
    model.load_weights('app/models/xi.h5')
    model.compile(optimizer='adam', loss=tf.losses.BinaryCrossentropy())

    img = cv.imread("C:/Users/zhutz/Documents/caller-8413-bot/download.jpg")
    img = tf.image.resize(img, (180,180))
    yhat = float(model.predict(np.expand_dims(img / 255, 0)))
    return yhat >= 0.5
