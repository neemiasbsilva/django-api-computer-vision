from django import forms
from .models import ImageUploadModel
from .models import ImageCropModel
from .models import BackgroundSubtractModel
from .models import BinarizeModel
from .models import CaptureModel

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()


class ImageUploadModel(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document')

class ImageCropForm(forms.ModelForm):
    class Meta:
        model = ImageCropModel
        fields = ('x', 'y', 'width', 'height', 'image')

class BackgroundSubtractForm(forms.ModelForm):
    class Meta:
        model = BackgroundSubtractModel
        fields = ('oimg', 'img')

class BinarizeForm(forms.ModelForm):
    class Meta:
        model = BinarizeModel
        fields = ('r', 'g', 'b','k', 'img')

class StreamForm(forms.Form):
    name = forms.CharField(max_length=55)

class CaptureForm(forms.ModelForm):
    class Meta:
        model = CaptureModel
        fields = ('image_name', )