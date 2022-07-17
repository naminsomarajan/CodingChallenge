from distutils.command.upload import upload
from django.db import models

# Create your models here.
class images(models.Model):
    image_name=models.CharField(max_length=100)
    image_description=models.CharField(max_length=255)
    images=models.ImageField(upload_to='UploadImages')
    