from django.urls import path, include
from .views import *

app_name = "driver"

urlpatterns = [
    path('driver/', DriverCreateView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('driver/<int:pk>', DriverDetailView.as_view()),
]
