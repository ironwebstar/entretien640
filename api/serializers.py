# coding=utf-8
from rest_framework import serializers
from . import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('email', 'first_name', 'last_name', 'city', 'cell_phone', 'customer_type', 'frequency', 'assign_to')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('email', 'first_name', 'last_name', 'position', 'Supervisor', 'email', 'cell_phone', 'note')
