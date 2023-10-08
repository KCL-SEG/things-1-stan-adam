from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(Model):
    name = models.CharField(
        max_length=30, 
        unique=True, 
        blank=False)
    description = models.CharField(
        unique=False, 
        max_length=120, 
        blank=True)
    quantity = models.PositiveIntegerField(
        unique=False, 
        validators=[
            MaxValueValidator(100),
        ]
        )
