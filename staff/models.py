
from django.db import models
class Staff(models.Model):
    name=models.CharField(max_length=100)
    qulification=models.CharField(max_length=100)
    experience=models.TextField()
    specialization=models.CharField()
    def __str__(self): return self.name