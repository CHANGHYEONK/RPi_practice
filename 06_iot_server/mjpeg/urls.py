from django.urls import path
from mjpeg.views import *

urlpatterns = [
    path('snapshot/', snapshot, name='snapshot'),
    path('stream/', stream, name='stream'),
]