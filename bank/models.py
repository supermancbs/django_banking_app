from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    balance = models.IntegerField()

class Withdrawl(models.Model):
    user = models.ForeignKey(User, related_name='withdrawls')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Deposit(models.Model):
    user = models.ForeignKey(User, related_name='deposits')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_money')
    reciever = models.ForeignKey(User, related_name='recieved_money')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
