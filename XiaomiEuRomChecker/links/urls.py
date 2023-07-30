from django.urls import path, include
from .views import LinkCreateView, LinkDeleteView, LinkDetailsView, LinkEditView, MyLinksView

urlpatterns = [
    path("<int:user_id>/link/", include([
        path('my_links/', MyLinksView.as_view(), name="my_links"),
        path("link_add/", LinkCreateView.as_view(), name="link_add"),
        path('link_details/<slug:slug>/', LinkDetailsView.as_view(), name="link_details"),
        path("link_edit/<slug:slug>/", LinkEditView.as_view(), name="link_edit"),
        path("link_delete/<slug:slug>/", LinkDeleteView.as_view(), name="link_delete"),
    ]), ),
]
