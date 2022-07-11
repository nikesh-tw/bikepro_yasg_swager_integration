from django.contrib.auth.models import User
from django.db import models


class BikeDetail(models.Model):
    name =  models.CharField(max_length=150)
    bike_number = models.CharField(max_length=150,unique=True)
    employee_id  = models.IntegerField(unique=True)

    def __str__(self):
        return f"Bike Number - {self.bike_number}, name - {self.name}"


