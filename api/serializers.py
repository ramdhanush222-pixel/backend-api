from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'doctor', 'date', 'time', 'status']
        read_only_fields = ['status']
