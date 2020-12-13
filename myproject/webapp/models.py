from django.db import models

from rest_framework.response import Response
# from . serializers import employeesSerializer

# Create your models here.
class employees(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    user_email  = models.EmailField(max_length=255,unique=True, blank=True)
    postal_address = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname
