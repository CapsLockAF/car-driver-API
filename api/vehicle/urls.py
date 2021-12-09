from django.urls import path, include
from .views import *

app_name = "vehicle"

urlpatterns = [
    path('vehicle/?with_drivers=<str:flag>/', VehicleWithDriverView.as_view({
        'get': 'list'
    })),
    path('vehicle/', VehicleCreateView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('vehicle/<int:pk>', VehicleDetailView.as_view()),

    path('set_driver/<int:pk>/', SetDriverView.as_view({
        'post': 'set_driver'})),



]
