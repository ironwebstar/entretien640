
from rest_framework import generics
from rest_framework.response import Response

from . import models
from . import serializers

class CustomUserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
