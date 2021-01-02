from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('search/', views.searchbar, name = 'searchbar'),
]