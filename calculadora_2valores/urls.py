from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc2, name='calc2')
]