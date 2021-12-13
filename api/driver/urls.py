from django.urls import path
from .views import *

app_name = "driver"

urlpatterns = [
    path('driver/', drivers_list),
    path('driver/<int:pk>', DriverDetailView.as_view()),
]
