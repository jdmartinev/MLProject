from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files import File


from .models import ML_Model
from .models import petsModel
from .forms import petsForm

import os
import tensorflow as tf
#from tensorflow import keras
from PIL import Image
import numpy as np


# Create your views here.

def home(request):
    #return HttpResponse('<h1> Welcome to Home Page</h1>')
    petModel = ML_Model.objects.filter(priority=1)[0]
    path = petModel.modelFile.path   
    model = tf.keras.models.load_model(path)

        
    if request.method == 'POST':  
        form = petsForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
             # Getting the current instance object to display in the template  
            
            img_object = form.instance 
            image = Image.open(img_object.image).convert('RGB')
            print(image.size)
            image = image.resize((150,150))
            print(image.size)
            image = np.array(image)  # Convert single image to
            image = np.expand_dims(image,0)
            pred = tf.keras.activations.sigmoid(model.predict(image))[0][0]
                     
            img_object.caption = f'dog prob {pred}, cat prob {1-pred}'
            
            return render(request, 'home.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = petsForm()  
  
    return render(request, 'home.html', {'form': form})  
 
        



    

