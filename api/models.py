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

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'
        ordering = ('id', )

class Client(CustomUser):

    is_admin = models.BooleanField(default=False)
    TYPE_VALUE = (
        ('Résidentiel', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Occasionnel', 'Occasionnel'),
    )
    customer_type = models.CharField(max_length=15, choices=TYPE_VALUE, blank=True)

    FREQUENCY_VALUE = (
        ('1x semaine', '1x semaine'),
        ('2x semaine', '2x semaine'),
        ('1x 2 semaines', '1x 2 semaines'),
        ('1x 3 semaines', '1x 3 semaines'),
        ('1x 4 semaines', '1x 4 semaines'),
    )
    frequency = models.CharField(max_length=15, choices=FREQUENCY_VALUE, blank=True)
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True)
    profit_month = models.IntegerField(blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'


class Prospect(CustomUser):
    last_contact = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=20)
    STAGES = (
        ('Nouveau', 'Nouveau'),
        ('Appel manqué #1', 'Appel manqué #1'),
        ('Appel manqué #2', 'Appel manqué #2'),
        ('Soumission RDV', 'Soumission RDV'),
        ('Soumission envoyée', 'Soumission envoyée'),
        ('Non intéressé', 'Non intéressé'),
        ('En attente', 'En attente'),
        ('Nouveau client', 'Nouveau client'),
    )
    # STAGES = (
    #     ('new customer', 'Nouveau'),
    #     ('missed_call_1', 'Appel manqué #1'),
    #     ('missed_call_2', 'Appel manqué #2'),
    #     ('rdv_submission', 'Soumission RDV'),
    #     ('submission_sent', 'Soumission envoyée'),
    #     ('no_interested', 'Non intéressé'),
    #     ('waiting', 'En attente'),
    #     ('new_customer', 'Nouveau client'),
    # )
    stage = models.CharField(max_length=15, choices=STAGES)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Prospects'
        verbose_name_plural = 'Prospects'
