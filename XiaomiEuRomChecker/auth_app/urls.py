from django.urls import path, include
from .views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = [
    path("auth/", include([
        path('register/', RegisterUserView.as_view(), name='register'),
        path('login/', LoginUserView.as_view(), name='login'),
        path('logout/', LogoutUserView.as_view(), name='logout'),
    ])),
]
