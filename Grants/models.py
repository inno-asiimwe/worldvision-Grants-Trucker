from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length = 200)
    physical_address = models.CharField(max_length = 200)
    email_address = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class SupportOffice(models.Model):
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
class Expenditure(models.Model):
    expenditure_text = models.CharField(max_length = 200)
    exp_date = models.DateTimeField('Date of Expenditure')
    amount = IntegerField('Amount spent')

    def __str__(self):
        return self.expenditure_text

class Payment(models.Model):
    payment_text = models.CharField(max_length = 200)
    pay_date = models.DateTimeField('Payment Date')
    amount = IntegerField('Amount paid')
