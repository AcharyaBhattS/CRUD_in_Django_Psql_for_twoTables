from django.db import models
from TestProject import settings

# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_code = models.CharField(max_length=100, null =True, blank=True)
    customer_name = models.CharField(max_length=100, null =True, blank=True)
    customer_room_no = models.IntegerField(null =True, blank=True)

    class Meta:
        db_table = 'customer_table'



class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # payment_date = models.DateField(null=True)
    payment_mode = models.CharField(max_length=100, null =True, blank=True)
    payment_amount = models.FloatField(max_length=200, null =True, blank=True)
    paid_customer_id = models.IntegerField(null =True, blank=True)
    paid_customer_code = models.CharField(max_length=100, null =True, blank=True)
    paid_cust_name = models.CharField(max_length=100, null =True, blank=True)
    paid_cust_room_no = models.IntegerField(null =True, blank=True)

    class Meta:
        db_table = 'payment_table'


