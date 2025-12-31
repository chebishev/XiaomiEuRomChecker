from django.urls import path

from .views import contact, downloads, index, thank_you

urlpatterns = [
    path('', index, name='index'),
    path('downloads/<int:pk>/<slug:slug>/', downloads, name='downloads'),
    path('contact/', contact, name='contact'),
    path('thank_you/', thank_you, name='thank_you'),
]
