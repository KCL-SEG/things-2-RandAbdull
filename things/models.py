from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=35, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(50)])

    created_at = models.DateTimeField(auto_now_add=True)
