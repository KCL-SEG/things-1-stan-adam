from django.db import models
from django.db.models import Model

class Thing(models):
    name = models.CharField(max_length=100)
    description = models.TextField
    quantity = models.IntegerField
