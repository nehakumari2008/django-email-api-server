from django.db import models
import json

# Create your models here.

class MyRegex(models.Model):
    regex = models.CharField(max_length=10000)
    label = models.CharField(max_length=100)

