from django.urls import path
from .views import index, downloads

urlpatterns = [
    path('', index, name='index'),
    path('downloads/<int:pk>/', downloads, name='downloads'),
]
