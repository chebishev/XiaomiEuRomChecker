from django.urls import path

from .views import ajax_devices, ajax_download, contact, index, thank_you

urlpatterns = [
    path("", index, name="index"),
    path("ajax/devices/", ajax_devices, name="ajax_devices"),
    path("ajax/download/", ajax_download, name="ajax_download"),
    path('contact/', contact, name='contact'),
    path('thank_you/', thank_you, name='thank_you'),
]
