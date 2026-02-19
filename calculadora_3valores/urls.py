from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc3, name='calc3')
]