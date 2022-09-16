from django.shortcuts import render
from gallery.models import Image
from .forms import *
from django.http import HttpResponseRedirect

def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = Image(  image = form.cleaned_data["image"],
                                name = form.cleaned_data["name"]
                                )
            new_image.save()
            return render(request, 'image_gallery.html', {'image': new_image})
            
def image_gallery(request):
    images = Image.objects.all().last()
    #print(images)
    return render(request, 'image_gallery.html', {'images': images})