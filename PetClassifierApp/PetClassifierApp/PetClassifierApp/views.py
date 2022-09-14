from django.shortcuts import render
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 

import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import os
from pathlib import Path


import datetime
import traceback

def index(request):
    if  request.method == "POST":
        f=request.FILES['sentFile'] # here you get the files needed
        file_name = "pic.jpg"
        file_name_2 = default_storage.save(file_name, f)
        base_dir =settings.MEDIA_ROOT
        my_file = os.path.join(base_dir,file_name_2) 
        image = tf.keras.preprocessing.image.load_img(my_file,target_size = (150,150,3))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])  # Convert single image to a batch.

        
        MLModel_DIR = os.path.join(settings.BASE_DIR,'MLModels','TransferLearningModel_Pets.h5')
        model = keras.models.load_model(MLModel_DIR)

        
        # get the predicted probabilities for each class
        pred = tf.keras.activations.sigmoid(model.predict(input_arr))
        if pred < 0.5:
            label = 'cat'
            prob = 1-pred
        else:
            label = 'dog'
            prob = pred
        response = {'label':label,'prob':prob}
        return render(request,'homepage.html',response)
    else:
        return render(request,'homepage.html')