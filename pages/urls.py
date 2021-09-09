from django.urls import path
from . import views

urlpatterns = [
    # Url to call to home_page function
    path('home', views.home_page),
    path('about', views.about_page),
]
