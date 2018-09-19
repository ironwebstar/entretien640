from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from users.models import CustomUser
# Create your models here.
class AdminUser(CustomUser):
    is_admin = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin User'

class Employee(CustomUser):
    is_admin = models.BooleanField(default=False)
    position = models.CharField(max_length=100, blank=True)
    Supervisor = models.CharField(max_length=100, blank=True)
    note = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

class Client(CustomUser):
    is_admin = models.BooleanField(default=False)
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
    profit_month = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

class Prospect(CustomUser):
    last_contact = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=20)
    STAGES = (
        ('missed_call_1', 'Missed call # 1'),
        ('missed_call_2', 'Missed call # 2'),
        ('rdv_submission', 'RDV submission'),
        ('submission_feels', 'Submission Feels'),
        ('new customer', 'New Customer'),
        ('no_interested', 'No Interested'),
        ('waiting', 'Waiting'),
    )
    stage = models.CharField(max_length=15, choices=STAGES)

    class Meta:
        verbose_name = 'Prospects'
        verbose_name_plural = 'Prospects'
