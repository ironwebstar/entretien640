
from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id', 'email', 'first_name', 'last_name', 'city', 'position', 'Supervisor',
                  'email', 'cell_phone', 'note')

class ClientSerializer(serializers.ModelSerializer):
    assign_to = serializers.PrimaryKeyRelatedField(read_only=True)
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['assign_to'] = EmployeeSerializer(instance.assign_to).data
        return response

    def to_internal_value(self, data):
        self.fields['assign_to'] = serializers.PrimaryKeyRelatedField(
            queryset=models.Employee.objects.all())
        return super(ClientSerializer, self).to_internal_value(data)

    class Meta:
        model = models.Client
        fields = ('id', 'email', 'first_name', 'last_name', 'city',
                  'cell_phone', 'customer_type', 'frequency', 'assign_to', 'profit_month')
        depth = 2

class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prospect
        fields = ('id', 'email', 'first_name', 'last_name', 'city', 'last_contact', 'ip_address', 'cell_phone', 'stage')
