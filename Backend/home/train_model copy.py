import os
import tensorflow as tf
import numpy as np
import cv2
MODEL_PATH = 'path_to_save_model/my_model.keras'  # Updated to use .keras format

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(100)
    ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
    return model

def load_model():
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)
        print("yes")
    else:
        model = create_model()
        print("No")

    return model

def train_model(new_image_path, new_label):
    model = load_model()
    model.summary()
    img = cv2.imread(new_image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = np.expand_dims(img, axis=-1)  
    new_label = np.array([new_label])
    images = np.array([img])
    model.fit(images, new_label, epochs=10)
    model.save(MODEL_PATH)
    score = model.evaluate(images, new_label, verbose=0)
    print('accuracy:', score[1],model)

def predict_fingerprint(image_path):
    model = load_model()
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (256, 256))
    img = np.expand_dims(img, axis=-1)
    images = np.array([img])
    predictions = model.predict(images)
    predicted_label = np.argmax(predictions[0])
    return predicted_label
