from django.contrib import admin
from django.urls import path, re_path, include
# from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mengine.urls'))
    # re_path('^$', views.homepage),
    # re_path('about/', views.about),
]
