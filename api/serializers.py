
from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"
        extra_kwargs = {'password': {'required': False}, 'username': {'required': False}}

class ClientSerializer(serializers.ModelSerializer):
    assign_to = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        try:
            response['assign_to'] = EmployeeSerializer(instance.assign_to).data
        except:
            response['assign_to'] = 4
        return response

    def to_internal_value(self, data):
        self.fields['assign_to'] = serializers.PrimaryKeyRelatedField(
            queryset=models.Employee.objects.all(), required=False)
        return super(ClientSerializer, self).to_internal_value(data)

    class Meta:
        model = models.Client
        fields = "__all__"
        depth = 2
        extra_kwargs = {'password': {'required': False}, 'username': {'required': False}}
        # extra_kwargs = {'assign_to': {'required': False}}
class ProspectSerializer(serializers.ModelSerializer):
    assign_to = serializers.PrimaryKeyRelatedField(read_only=True, required=False)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        try:
            response['assign_to'] = EmployeeSerializer(instance.assign_to).data
        except:
            response['assign_to'] = 5
        return response

    def to_internal_value(self, data):
        self.fields['assign_to'] = serializers.PrimaryKeyRelatedField(
            queryset=models.Employee.objects.all(), required=False)
        return super(ProspectSerializer, self).to_internal_value(data)

    class Meta:
        model = models.Prospect
        fields = "__all__"
        depth = 2
        extra_kwargs = {'password': {'required': False}, 'username': {'required': False}}