from django.urls import path, include
from .views import *

app_name = "vehicle"

urlpatterns = [
    path('vehicle/', VehicleCreateView.as_view()),
    path('vehicle/all/', VehicleListView.as_view()),
    path('vehicle/<int:pk>', VehicleDetailView.as_view())
]