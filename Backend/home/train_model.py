import fnmatch
import face_recognition as fr
import os
import numpy as np
import tensorflow as tf
import cv2
import os
import matplotlib.pyplot as plt
from tensorflow import keras
from matplotlib import pyplot as plt


model_path = "./CNN_model.h5"
model = keras.models.load_model(model_path)

def saveFingerData(img,name):

    img1 = cv2.imread('test_data/a.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('test_data/b.bmp', cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1, (256, 256))
img1 = np.expand_dims(img1, axis=-1)
img2 = cv2.resize(img2, (256, 256))
img2 = np.expand_dims(img2, axis=-1)

pred1 = model.predict(np.array([img1]))
pred2 = model.predict(np.array([img2]))

if np.argmax(pred1) == np.argmax(pred2):