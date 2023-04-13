from django.views.generic import TemplateView
from django.http import HttpResponse, StreamingHttpResponse
from .cvcam import MJpegStreamCam
from time import sleep

mjpegstream = MJpegStreamCam()

class CamView(TemplateView):
    template_name = "cam.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["mode"] = self.request.GET.get("mode", "#")
        return context
    

def snapshot(request):
    sleep(0.1)
    image = mjpegstream.snapshot()
    return HttpResponse(image, content_type="image/jpeg")


def stream(request):
    return StreamingHttpResponse(mjpegstream, 
    content_type='multipart/x-mixed-replace;boundary=--myboundary')