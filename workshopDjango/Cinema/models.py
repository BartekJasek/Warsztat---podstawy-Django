from django.db import models


# Create your models here.
class Hall(models.Model):
     hall_name = models.CharField(max_length=255)
     hall_size = models.IntegerField
     projector = models.BooleanField
