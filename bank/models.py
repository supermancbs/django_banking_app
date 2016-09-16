from __future__ import unicode_literals
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    balance = models.IntegerField()
    def lower_money(amount):
        self.balance-=amount
        self.save

class Withdrawal(models.Model):
    user = models.ForeignKey(User, related_name='withdrawals')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_lower = User.objects.get(user)
    user.lower_money(amount)

class Deposit(models.Model):
    user = models.ForeignKey(User, related_name='deposits')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_money')
    reciever = models.ForeignKey(User, related_name='recieved_money')
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
