from django.http import HttpResponse
from django.shortcuts import render

from .models import images

def index(request):
    dic_images={
           'images':images.objects.all()
          }
    return render(request,'index.html',dic_images)