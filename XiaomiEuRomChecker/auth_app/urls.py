from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView, \
    profile_details, profile_edit, ProfileDeleteView, my_device, update_telegram

urlpatterns = [
    path("auth/", include([
        path('register/', RegisterUserView.as_view(), name='register'),

        # redirect_authenticated_user=True will redirect logged users directly to the index
        path('login/', LoginUserView.as_view(redirect_authenticated_user=True), name='login'),
        path('logout/', LogoutUserView.as_view(), name='logout'),
    ])),
    path("profile/<int:pk>/", include([
        path('', profile_details, name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path("delete/", ProfileDeleteView.as_view(), name='profile_delete'),
        path("my_device/", my_device, name='my_device'),
    ])),
    path("update_telegram/", update_telegram, name='update_telegram'),
]
