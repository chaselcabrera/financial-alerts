from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Thresholds: allow for users to create unique thresholds for users
class Threshold(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    threshold_amount = models.DecimalField(max_digits=19, decimal_places=2)
    type = models.CharField(max_length=100)

# Alerts:  auto created when threshold are met during a transaction insert
class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    threshold = models.ForeignKey(Threshold, on_delete=models.CASCADE)
    message = models.TextField()

#Trasactions: user specific transactions including status
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    # status = models.BooleanField(default=1,db_index=True) Future field


# ThresholdType: Enables user to create thresholds that are speicfic to their use case i.e. budget, max-spend, etc.
# class ThresholdType(models.Model):
#     slug = models.SlugField(unique=True)
#     name = models.CharField(max_length=100)

# Transaction Cateogries:  user defined allow for anyone to add categories to a roaster of cateogiress (this might be better as a user defined value as users might not want to see cross account info) i.e. groceries, subscription, etc.
# class TransactionCategory(models.Model):
#     slug = models.SlugField(unique=True)
#     title = models.CharField(max_length=100)

# Tranaction types:  user defined allowing anyone to create new transaction types (this might also benifit from being user defined as cross account data could hinder UX) i.e. income, debt, credit, etc.
# class TransactionType(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True, default='')

