from django.urls import path, include
from .views import *

app_name = "driver"

urlpatterns = [
    path('driver/d1/', DriverCreateView.as_view()),
    path('driver/d2/', DriverListView.as_view()),
    path('driver/<int:pk>', DriverDetailView.as_view()),
]
