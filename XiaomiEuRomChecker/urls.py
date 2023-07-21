"""
URL configuration for XiaomiEuRomChecker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # path to core_app all urls
    path('', include('XiaomiEuRomChecker.core.urls')),

    # path to auth_app all urls
    path('', include('XiaomiEuRomChecker.auth_app.urls')),

    # path to links_app all urls
    path('links/', include('XiaomiEuRomChecker.links.urls')),
]
handler404 = 'XiaomiEuRomChecker.core.views.page_not_found'