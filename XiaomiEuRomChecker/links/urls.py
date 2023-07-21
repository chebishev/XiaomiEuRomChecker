from django.urls import path
from .views import LinkCreateView, LinkEditView, LinkDeleteView, link_details

urlpatterns = [
        path("link_add/", LinkCreateView.as_view(), name="link_add"),
        path('link_details/<slug:slug>/', link_details, name="link_details"),
        path("link_edit/<slug:slug>/", LinkEditView.as_view(), name="link_edit"),
        path("link_delete/<slug:slug>/", LinkDeleteView.as_view(), name="link_delete"),
]
