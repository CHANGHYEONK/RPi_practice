from django.views.generic import TemplateView
from django.http import HttpResponse, StreamingHttpResponse
from .cvcam import MJpegStreamCam


mjpegstream = MJpegStreamCam()

def snapshot(request):
    image = mjpegstream.snapshot()
    return HttpResponse(image, content_type="image/jpeg")

def stream(request):
    return StreamingHttpResponse(mjpegstream, 
    content_type='multipart/x-mixed-replace;boundary=--myboundary')