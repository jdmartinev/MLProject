import tensorflow as tf
from tensorflow import keras
from PIL import Image
import sys
import numpy as np

model_path = sys.argv[1]
file_path = sys.argv[2]


model = keras.models.load_model(model_path)


image = tf.keras.preprocessing.image.load_img(file_path,target_size = (150,150,3))
input_arr = tf.keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.


pred = tf.keras.activations.sigmoid(model.predict(input_arr))
if pred < 0.5:
  label = 'cat'
  prob = 1-pred
else:
  label = 'dog'
  prob = pred


print(f'The pet is a {label} with probability {prob}')