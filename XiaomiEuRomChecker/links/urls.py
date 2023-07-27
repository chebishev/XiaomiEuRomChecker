from django.urls import path, include
from .views import LinkCreateView, LinkEditView, LinkDeleteView, LinkDetailsView

urlpatterns = [
    path("<int:user_id>/link/", include([
        path("link_add/", LinkCreateView.as_view(), name="link_add"),
        path("<slug:slug>/", include([
            path('link_details/', LinkDetailsView.as_view(), name="link_details"),
            path("link_edit/", LinkEditView.as_view(), name="link_edit"),
            path("link_delete/", LinkDeleteView.as_view(), name="link_delete"),
        ])),

    ]), ),
]
