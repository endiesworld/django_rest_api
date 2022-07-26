"""movie_db URL Configuration

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

from unicodedata import name
from django.urls import path
# from movie_app.api.views import movie_list, movie_detials
from movie_app.api.views import WatchListDetailsAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailsAV

urlpatterns = [
    path('movies/', WatchListAV.as_view(), name='list of all movies'),
    path('movies/<int:pk>',  WatchListDetailsAV.as_view(), name='movie details'),
    path('stream',  StreamPlatformAV.as_view(), name='stream platform'),
    path('stream/<int:pk>',  StreamPlatformDetailsAV.as_view(),
         name='stream platform details')
]
