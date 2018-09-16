from django.db import models
from users.models import CustomUser
# Create your models here.

class Employee(CustomUser):
    position = models.CharField(max_length=100, blank=True)
    Supervisor = models.CharField(max_length=100, blank=True)
    note = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

class Client(CustomUser):

    TYPE_VALUE = (
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Occasionnel', 'Occasionnel'),
    )
    customer_type = models.CharField(max_length=15, choices=TYPE_VALUE)

    FREQUENCY_VALUE = (
        ('1x_semaine', '1x semaine'),
        ('1x_2_semaines', '1x 2 semaines'),
        ('1x_3_semaines', '1x 3 semaines'),
        ('1x_mois', '1x mois'),
    )
    frequency = models.CharField(max_length=15, choices=FREQUENCY_VALUE)
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'
