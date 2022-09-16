from django.shortcuts import render
from django.http import HttpResponse

import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
from PIL import Image
import numpy as np




def home(request):
    model = tf.keras.models.load_model('static/TransferLearningModel_Pets.h5')
    
    if request.method =='POST':
        handle_uploaded_file(request.FILES['sentFile'])
        image = tf.keras.preprocessing.image.load_img('static/test.jpg',target_size = (150,150,3))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to a batch.
        pred = tf.keras.activations.sigmoid(model.predict(input_arr))[0][0]
        caption = f'dog prob {pred}, cat prob {1-pred}'

        return render(request, 'home.html',{'caption':caption})
    else:
        return render(request, 'home.html')

def handle_uploaded_file(f):
    with open('static/test.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)