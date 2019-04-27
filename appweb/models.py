from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CExpense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
        # return self.text


class CIncome(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.date, self.amount)
