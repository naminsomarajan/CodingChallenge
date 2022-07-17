
from django.contrib import admin
from django.urls import path


from GalleryApp import views

urlpatterns = [
    path('',views.index),
]
