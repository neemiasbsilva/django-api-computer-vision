from django.shortcuts import render
from .forms import UploadImageForm, ImageUploadModel, ImageCropForm, BackgroundSubtractForm
from .forms import BinarizeForm, StreamForm, CaptureForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .opencv_dface import opencv_dface
from .crop_image import crop_image
from .subtract import subtract
from .binarize_mask import binarize_mask
from .stream_video import stream_video
from .capture_image import capture_image
from django.http import HttpResponseRedirect
# Create your views here.


def first_view(request):
    return render(request, 'pipeline/first_view.html', {})


def webcam(request):
    if request.method == 'POST':
        return render(request, 'pipeline/webcam.html', {})
    else:
        return render(request, 'pipeline/webcam.html', {})
def uimage(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            upload_file_url = fs.url(filename)
            return render(request, 'pipeline/uimage.html',
                      {'form': form, 'upload_file_url': upload_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'pipeline/uimage.html',
                      {'form':form})


def dface(request):
    if request.method == 'POST':
        form = ImageUploadModel(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            opencv_dface(settings.MEDIA_ROOT_URL + imageURL)
            return render(request, 'pipeline/dface.html',
                          {'form': form, 'post': post})
    else:
        form = ImageUploadModel()

        return render(request, 'pipeline/dface.html',
                      {'form': form})


def crop(request):
    if request.method == 'POST':
        form = ImageCropForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            #image = request.FILES['image']
            x = int(request.POST['x'])
            y = int(request.POST['y'])
            width = int(request.POST['width'])
            height = int(request.POST['height'])
            imageURL = settings.MEDIA_URL + form.instance.image.name
            crop_image(settings.MEDIA_ROOT_URL + imageURL, x, y, width, height)

            return render(request, 'pipeline/crop.html',
                          {'form': form, 'post': post})
    else:
        form = ImageCropForm()
        return render(request, 'pipeline/crop.html', {'form': form})


def backgroundsubtract(request):
    if request.method == 'POST':
        form = BackgroundSubtractForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.save()

            imageURL1 = settings.MEDIA_URL + form.instance.oimg.name
            imageURL2 = settings.MEDIA_URL + form.instance.img.name

            subtract(settings.MEDIA_ROOT_URL+imageURL1, settings.MEDIA_ROOT_URL + imageURL2)

            return render(request, 'pipeline/backgroundsubtract.html',
                          {'form': form, 'post': post})
    else:
        form = BackgroundSubtractForm()
        return render(request, 'pipeline/backgroundsubtract.html',
                      {'form': form})


def binarize(request):
    if request.method == 'POST':
        form = BinarizeForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.save()

            r = float(request.POST['r'])
            g = float(request.POST['g'])
            b = float(request.POST['b'])
            k = float(request.POST['k'])
            imageURL = settings.MEDIA_URL + form.instance.img.name

            binarize_mask(settings.MEDIA_ROOT_URL + imageURL, r, g, b, k)

            return render(request, 'pipeline/binarize.html',
                          {'form': form, 'post': post})

    else:
        form = BinarizeForm()

        return render(request, 'pipeline/binarize.html',
                      {'form': form})

def stream(request):

    if request.method == 'POST':

        form = StreamForm(request.POST, request.FILES)
        if form.is_valid():

            stream_video()
            return HttpResponseRedirect(request.path_info)

    else:
        form = StreamForm()
        return render(request, 'pipeline/stream.html',{'form':form})

def capture(request):

    if request.method == 'POST':

        form = CaptureForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            imageURL = settings.MEDIA_ROOT_URL + settings.MEDIA_URL + 'image.jpg'
            capture_image(imageURL)
            return render(request, 'pipeline/capture.html',
                          {'form': form, 'post':post})
    else:
        form = CaptureForm()
        return render(request, 'pipeline/capture.html',
                      {'form': form})