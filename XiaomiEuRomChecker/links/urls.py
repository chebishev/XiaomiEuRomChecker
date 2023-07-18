from django.urls import path
from .views import LinksDetailView, LinkCreateView, LinkEditView, LinkDeleteView


urlpatterns = [
    path('user_links/', LinksDetailView.as_view(), name="links"),
    path("link_add/", LinkCreateView.as_view(), name="link_add"),
    path("link_edit/", LinkEditView.as_view(), name="link_edit"),
    path("link_delete/", LinkDeleteView.as_view(), name="link_delete"),
]
