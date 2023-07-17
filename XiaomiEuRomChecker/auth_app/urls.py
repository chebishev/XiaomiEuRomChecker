from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView, \
    ProfileDetailsView, profile_edit, ProfileDeleteView

urlpatterns = [
    path("auth/", include([
        path('register/', RegisterUserView.as_view(), name='register'),
        path('login/', LoginUserView.as_view(), name='login'),
        path('logout/', LogoutUserView.as_view(), name='logout'),
    ])),
    path("profile/<int:pk>/", include([
        path('', ProfileDetailsView.as_view(), name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path("delete/", ProfileDeleteView.as_view(), name='profile_delete'),
    ]))
]
