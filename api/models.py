from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Expense Title ' + str(self.name) + ' Amount: ' + str(self.amount)

    class Meta:
        ordering = ['-timestamp']