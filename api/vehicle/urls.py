from django.urls import path, include
from .views import *

app_name = "vehicle"

urlpatterns = [
    path('vehicle/', VehicleCreateView.as_view()),
]