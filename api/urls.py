from django.urls import path

from . import views

urlpatterns = [
    path('shorten', views.UrlShortenerView.post),
    path('<str:shorturl>', views.UrlShortenerView.get),

]