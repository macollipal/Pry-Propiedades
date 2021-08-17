from abc import abstractmethod
from django.db import models

from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_by = models.IntegerField(blank=True, null=True)
    
    class Meta:
        abstract =True

# Create your models here.
