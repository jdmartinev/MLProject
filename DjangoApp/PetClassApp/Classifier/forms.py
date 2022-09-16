from django.db import models  
from django.forms import fields  
from .models import petsModel  
from django import forms  
      
      
class petsForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = petsModel  
        # It includes all the fields of model  
        fields = '__all__'  