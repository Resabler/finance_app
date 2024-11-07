from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    transaction_type=models.CharField(max_length=20,choices=TRANSACTION_TYPE_CHOICES)
    date=models.DateField()
    description=models.CharField(max_length=20)

class Budget(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    month=models.DateField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)    
