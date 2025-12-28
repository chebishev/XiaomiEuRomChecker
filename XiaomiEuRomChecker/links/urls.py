from django.urls import path, include
from .views import LinkCreateView, LinkDeleteView, LinkDetailsView, LinkEditView, MyLinksView

urlpatterns = [
    path("link_add/", LinkCreateView.as_view(), name="link_add"),
    # all links are with prefix links/user_id/link/
    path("<int:user_id>/", include([

        # links that don't need slug
        path('my_links/', MyLinksView.as_view(), name="my_links"),

        # links that need slug
        path('link_details/<slug:slug>/', LinkDetailsView.as_view(), name="link_details"),
        path("link_edit/<slug:slug>/", LinkEditView.as_view(), name="link_edit"),
        path("link_delete/<slug:slug>/", LinkDeleteView.as_view(), name="link_delete"),
    ]), ),
]
