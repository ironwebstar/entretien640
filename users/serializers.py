from rest_framework import serializers
from . import models

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', 'bio', 'location' ,'birth_date', 'house_phone', 'cell_phone', 'postal_address'
                  'city', 'province', 'pays')