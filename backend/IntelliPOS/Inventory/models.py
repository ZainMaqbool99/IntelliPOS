from turtle import ondrag
from django.db import models

class Category(models.Model):
    CId = models.AutoField(primary_key=True)
    CName = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)

class Brands(models.Model):
    BId = models.AutoField(primary_key=True)
    BName = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)

class ItemSetup(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=500)
    CId = models.ForeignKey(Category, db_column='CId', on_delete=models.DO_NOTHING)
    BId = models.ForeignKey(Brands, db_column='BId', on_delete=models.DO_NOTHING)
    RPrice = models.DecimalField(decimal_places=2, max_digits=10)
    SPrice = models.DecimalField(decimal_places=2, max_digits=10)
    BarCode = models.CharField
    isActive = models.BooleanField(default=True)

class Opening(models.Model):
    OPId = models.AutoField(primary_key=True)
    OPDate = models.DateTimeField()
    ItemId = models.ForeignKey(ItemSetup, db_column = 'ItemId', on_delete=models.DO_NOTHING)
    BatchNo = models.CharField(max_length=100)
    Qty = models.IntegerField()

class Purchase(models.Model):
    PId = models.AutoField(primary_key=True)
    PDate = models.DateTimeField()
    ItemId = models.ForeignKey(ItemSetup, db_column='ItemId', on_delete=models.DO_NOTHING)
    BatchNo = models.CharField(max_length=100)
    Qty = models.IntegerField()

class Stock(models.Model):
    SId = models.AutoField(primary_key=True)
    ItemId = models.ForeignKey(ItemSetup, db_column='ItemId', on_delete=models.DO_NOTHING)
    ItemName = models.CharField(max_length=500)
    BatchNo = models.CharField
    Qty = models.IntegerField()





