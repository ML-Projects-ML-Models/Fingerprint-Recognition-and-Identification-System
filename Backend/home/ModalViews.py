from django.conf import settings
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

model = keras.models.load_model(settings.MODELS_FINGER_PATH)
print(model)