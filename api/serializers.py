# coding=utf-8
from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id', 'email', 'first_name', 'last_name', 'city', 'position', 'Supervisor', 'email', 'cell_phone', 'note')

class ClientSerializer(serializers.ModelSerializer):

    assign_to = EmployeeSerializer(read_only=True, many=False)

    class Meta:
        model = models.Client
        fields = ('id', 'email', 'first_name', 'last_name', 'city',
                  'cell_phone', 'customer_type', 'frequency', 'assign_to', 'profit_month')