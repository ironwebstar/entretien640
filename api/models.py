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
    EMPLOYEE_POST = (
        ('Préposé entretien ménager', 'Préposé entretien ménager'),
        ('Superviseur', 'Superviseur'),
        ('Administrateur', 'Administrateur'),
    )
    PREFERENTIAL_PAYMENT_METHOD = (
        ('Argent comptant', 'Argent comptant'),
        ('Chèque', 'Chèque'),
        ('Dépôt direct', 'Dépôt direct'),
    )
    ANIMALS = (
        ('Chat', 'Chat'),
        ('Oiseaux', 'Oiseaux')
    )

    is_admin = models.BooleanField(default=False)
    position = models.CharField(max_length=100, blank=True)
    Supervisor = models.CharField(max_length=100, blank=True)
    note = models.TextField(max_length=500, blank=True)
    login_email = models.CharField(max_length=100, blank=True)
    hourly_salary = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, default='#FFF')
    remarks = models.TextField(max_length=500, blank=True)
    employee_post = models.CharField(max_length=45, choices=EMPLOYEE_POST, blank=True)
    pre_payment_method = models.CharField(max_length=45, choices=PREFERENTIAL_PAYMENT_METHOD, blank=True)
    animals = models.CharField(max_length=20, choices=ANIMALS, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'
        ordering = ('id', )

class Client(CustomUser):

    TYPE_VALUE = (
        ('Résidentiel', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Occasionnel', 'Occasionnel'),
    )
    ESTIMATED_VALUE = (
        ('1 heure et demi', '1 heure et demi'), ('2 heures', '2 heures'),
        ('2 heures et demi', '2 heures et demi'), ('3 heures', '3 heures'),
        ('3 heures et demi', '3 heures et demi'), ('4 heures', '4 heures'),
        ('4 heures et demi', '4 heures et demi'), ('5 heures', '5 heures'),
        ('5 heures et demi', '5 heures et demi'), ('6 heures', '6 heures'),
        ('6 heures et demi', '6 heures et demi'), ('7 heures', '7 heures'),
        ('7 heures et demi', '7 heures et demi'), ('8 heures', '8 heures'),
        ('8 heures et demi', '8 heures et demi'), ('9 heures', '9 heures'),
        ('9 heures et demi', '9 heures et demi'), ('10 heures', '10 heures'),
    )
    FREQUENCY_VALUE = (
        ('1x semaine', '1x semaine'),
        ('2x semaine', '2x semaine'),
        ('1x 2 semaines', '1x 2 semaines'),
        ('1x 3 semaines', '1x 3 semaines'),
        ('1x 4 semaines', '1x 4 semaines'),
    )
    REPLACEMENT_OPTION = (
        ('Reporté le ménage', 'Reporté le ménage'),
        ('Envoyé un remplaçant', 'Envoyé un remplaçant'),
    )
    DAYS_OPTION = (
        ('Lun', 'Lun'), ('Mar', 'Mar'), ('Mer', 'Mer'),
        ('Jeu', 'Jeu'), ('Ven', 'Ven'), ('Sam', 'Sam'),
        ('Dim' ,'Dim'),
    )
    PAYMENT_OPTION = (
        ('Virement Interac', 'Virement Interac'), ('Argent comptant', 'Argent comptant'),
        ('Dépôt direct', 'Dépôt direct'), ('Chèque', 'Chèque'), ('Carte de crédit', 'Carte de crédit'),
    )
    customer_type = models.CharField(max_length=15, choices=TYPE_VALUE, blank=True)
    is_admin = models.BooleanField(default=False)
    frequency = models.CharField(max_length=15, choices=FREQUENCY_VALUE, blank=True)
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, default=1)
    profit_month = models.IntegerField(blank=True, null=True)
    login_email = models.EmailField(blank=True, max_length=100)
    estimated_time = models.CharField(max_length=15, choices=ESTIMATED_VALUE, blank=True)
    replacement = models.CharField(max_length=30, choices=REPLACEMENT_OPTION, blank=True)
    days = models.CharField(max_length=5, choices=DAYS_OPTION, blank=True)
    code_key = models.CharField(max_length=100, blank=True)
    animals = models.CharField(max_length=100, blank=True)
    payment = models.CharField(max_length=30, choices=PAYMENT_OPTION, blank=True)
    remarks = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

class Prospect(CustomUser):
    last_contact = models.DateTimeField(auto_now=True, blank=True)
    ip_address = models.CharField(max_length=20, blank=True)
    ESTIMATED_VALUE = (
        ('1 heure et demi', '1 heure et demi'), ('2 heures', '2 heures'),
        ('2 heures et demi', '2 heures et demi'), ('3 heures', '3 heures'),
        ('3 heures et demi', '3 heures et demi'), ('4 heures', '4 heures'),
        ('4 heures et demi', '4 heures et demi'), ('5 heures', '5 heures'),
        ('5 heures et demi', '5 heures et demi'), ('6 heures', '6 heures'),
        ('6 heures et demi', '6 heures et demi'), ('7 heures', '7 heures'),
        ('7 heures et demi', '7 heures et demi'), ('8 heures', '8 heures'),
        ('8 heures et demi', '8 heures et demi'), ('9 heures', '9 heures'),
        ('9 heures et demi', '9 heures et demi'), ('10 heures', '10 heures'),
    )
    FREQUENCY_VALUE = (
        ('1x semaine', '1x semaine'),
        ('2x semaine', '2x semaine'),
        ('1x 2 semaines', '1x 2 semaines'),
        ('1x 3 semaines', '1x 3 semaines'),
        ('1x 4 semaines', '1x 4 semaines'),
    )
    REPLACEMENT_OPTION = (
        ('Reporté le ménage', 'Reporté le ménage'),
        ('Envoyé un remplaçant', 'Envoyé un remplaçant'),
    )
    DAYS_OPTION = (
        ('Lun', 'Lun'), ('Mar', 'Mar'), ('Mer', 'Mer'),
        ('Jeu', 'Jeu'), ('Ven', 'Ven'), ('Sam', 'Sam'),
        ('Dim' ,'Dim'),
    )
    PAYMENT_OPTION = (
        ('Virement Interac', 'Virement Interac'), ('Argent comptant', 'Argent comptant'),
        ('Dépôt direct', 'Dépôt direct'), ('Chèque', 'Chèque'), ('Carte de crédit', 'Carte de crédit'),
    )
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
    is_admin = models.BooleanField(default=False)
    frequency = models.CharField(max_length=15, choices=FREQUENCY_VALUE, blank=True)
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True, default=1)
    profit_month = models.IntegerField(blank=True, null=True)
    login_email = models.EmailField(blank=True, max_length=100)
    estimated_time = models.CharField(max_length=15, choices=ESTIMATED_VALUE, blank=True)
    replacement = models.CharField(max_length=30, choices=REPLACEMENT_OPTION, blank=True)
    days = models.CharField(max_length=5, choices=DAYS_OPTION, blank=True)
    code_key = models.CharField(max_length=100, blank=True)
    animals = models.CharField(max_length=100, blank=True)
    payment = models.CharField(max_length=30, choices=PAYMENT_OPTION, blank=True)
    stage = models.CharField(max_length=15, choices=STAGES, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Prospects'
        verbose_name_plural = 'Prospects'

