from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='calc3_home')
]