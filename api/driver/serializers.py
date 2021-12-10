from rest_framework import serializers
from .models import Driver


class DriverDetailSerializer(serializers.ModelSerializer):
    """define the Driver API representation"""
    class Meta:
        model = Driver
        fields = '__all__'
