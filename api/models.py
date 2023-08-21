from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=10)

