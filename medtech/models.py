from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField
    address = models.CharField

class Country(models.Model):
    name = models.CharField