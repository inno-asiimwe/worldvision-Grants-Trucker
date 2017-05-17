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

    def __str__(self):
        return self.payment_text

class Project(models.Model):
    name = models.CharField(max_length = 200)
    project_identifier = models.CharField(max_length = 200)
    donor = models.ForeignKey(Donor, on_delete = models.CASCADE)
    support_office = models.ForeignKey(SupportOffice, on_delete = models.CASCADE)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End Date')
    status = models.CharField(max_length =  50)
    description = models.CharField(max_length = 200)
    expenditure =  models.ForeignKey(Expenditure, on_delete = models.CASCADE)
    payment = models.ForeignKey(Expenditure, on_delete = models.CASCADE)
    grant_amount = models.IntegerField('Grant Amount')

    def __str__(self):
        return self.name

        
