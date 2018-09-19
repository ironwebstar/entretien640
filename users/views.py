from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import exceptions

from . import models
from . import serializers

class CustomUserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer

