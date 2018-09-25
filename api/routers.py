# coding=utf-8
from rest_framework import routers
from .viewsets import EmployeeViewSet, ClientViewSet, ProspectViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'client', ClientViewSet)
router.register(r'prospect', ProspectViewSet)