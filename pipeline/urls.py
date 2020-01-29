from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'),
    url(r'^dface/$', views.dface, name='dface'),
    url(r'^crop/$', views.crop, name='crop'),
    url(r'^backgroundsubtract/$', views.backgroundsubtract, name='backgroundsubtract'),
    url(r'^binarize/$', views.binarize, name='binarize'),
    url(r'^webcam/$', views.webcam, name='webcam'),
    url(r'^stream/$', views.stream, name='stream'),
    url(r'^capture/$', views.capture, name='capture'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)