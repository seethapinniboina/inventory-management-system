from django.db import models

# Create your models here.
class Inventory(models.Model):
    Id =  models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    IIN = models.CharField(max_length=10, null=True, blank=True)
    Cost = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    Quantity = models.PositiveIntegerField(null=True, blank=True, default=0)
    Quantity_sold = models.PositiveIntegerField(null=True, blank=True, default=0)
    Selling_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    Item_profit = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    Profit_earned = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10, default=0)
    Revenue = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10, default=0)
    
class Order(models.Model):
    Id =  models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Item = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    Quantity = models.PositiveIntegerField(null=True, blank=True)
    Cost = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    Orderdttm = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    Is_received = models.BooleanField(default=False)
    Is_cancel = models.BooleanField(default=False)

class Transaction(models.Model):
    Id =  models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Item = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    Quantity = models.PositiveIntegerField(null=True, blank=True)
    Selling_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)
    Transactiondttm = models.DateTimeField(null=True, blank=True, auto_now_add=True)