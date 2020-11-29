from django.urls import path, include

from . import views

app_name = 'fileupdownld'
urlpatterns = [
    path('', views.index, name="index"),
]
