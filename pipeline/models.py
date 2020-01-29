from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ImageCropModel(models.Model):
    x = models.CharField(max_length=255, blank=True)
    y = models.CharField(max_length=255, blank=True)
    width = models.CharField(max_length=255, blank=True)
    height = models.CharField(max_length=255, blank=True)

    image = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class BackgroundSubtractModel(models.Model):
    oimg = models.ImageField(upload_to='images/%Y/%m/%d')
    img = models.ImageField(upload_to='images/%Y/%m/%d')

    uploaded_at = models.DateTimeField(auto_now_add=True)


class BinarizeModel(models.Model):
    r = models.CharField(max_length=20, blank=True)
    g = models.CharField(max_length=20, blank=True)
    b = models.CharField(max_length=20, blank=True)
    k = models.CharField(max_length=20, blank=True)
    img = models.ImageField(upload_to='images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class CaptureModel(models.Model):
    #img = models.ImageField()
    image_name = models.CharField(max_length=20, blank=True)