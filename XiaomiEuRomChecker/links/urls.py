from django.urls import path, include
from .views import LinkCreateView, LinkDeleteView, LinkDetailsView, link_edit

urlpatterns = [
    path("<int:user_id>/link/", include([
        path("link_add/", LinkCreateView.as_view(), name="link_add"),
        path('link_details/<slug:slug>/', LinkDetailsView.as_view(), name="link_details"),
        path("link_edit/<slug:slug>/", link_edit, name="link_edit"),
        path("link_delete/<slug:slug>/", LinkDeleteView.as_view(), name="link_delete"),
    ]), ),
]
