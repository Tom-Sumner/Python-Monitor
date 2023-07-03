from django.db import models
from accounts.models import Employee


class Computer(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    anydesk = models.IntegerField()
    user = models.OneToOneField(Employee, models.CASCADE)
    password = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.model}"