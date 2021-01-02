from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.homepage),
    re_path('about/', views.about),
]
