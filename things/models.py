from django.db import models
from models import Model

class Thing(Model):
    name = models.CharField()
    description = models.TextField
    quantity = models.IntegerField
