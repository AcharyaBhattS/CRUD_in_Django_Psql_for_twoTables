from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    room_no = models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer'


class Invoice(models.Model):
    bill_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    bill_date = models.DateField()
    amount_paid = models.FloatField()

    class Meta:
        managed = False
        db_table = 'invoice'