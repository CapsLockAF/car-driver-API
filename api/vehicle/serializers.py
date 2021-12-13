from rest_framework import serializers
from .models import Vehicle


class VehicleDetailSerializer(serializers.ModelSerializer):
    """define the Driver API representation"""
    class Meta:
        model = Vehicle
        fields = '__all__'


class SetDriverSerializer(serializers.ModelSerializer):
    """define the Driver API (set driver in a car ) representation"""
    class Meta:
        model = Vehicle
        fields = ['driver_id']
