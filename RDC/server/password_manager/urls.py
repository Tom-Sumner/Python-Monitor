"""password_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as AuthViews

from users import urls as UserUrls
from computer import urls as computerUrls
from other import urls as otherUrls
from accounts import urls as accountsUrls
from instructions import urls as insUrls

urlpatterns = [
    path("", include(computerUrls), name="computer"),
    path('admin/', admin.site.urls),
    path("users/", include(UserUrls), name="users"),
    path("other/", include(otherUrls), name="other"),
    path("accounts/", include(accountsUrls), name="accounts"),
    path("instructions/", include(insUrls), name="instructions")
]
