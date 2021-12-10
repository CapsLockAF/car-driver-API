from django.urls import path
from .views import *

app_name = "vehicle"

urlpatterns = [
    path('vehicle/', vehicles_list),
    path('vehicle/<int:pk>', VehicleDetailView.as_view()),

    path('set_driver/<int:pk>/', SetDriverView.as_view({
        'post': 'set_driver'})),
]
