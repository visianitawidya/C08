"""C08 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

import home.urls as home
import event.urls as event
import leaderboard.urls as leaderboard
import profile_dashboard.urls as profile
import login_form.urls as loginform

from home.views import index as index_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home)),
    path('signup/', include(loginform)),
    path('profile/', include(profile)),
    re_path(r'^$', index_home, name='index')
]
