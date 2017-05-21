from django.db import models
from django.utils import timezone

# Create your models here.

class SupportOffice(models.Model):
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Project(models.Model):
    """model class for the project table in the database,all information about the project can be derived from here"""
    project_name = models.CharField(max_length = 200)
    project_identifier = models.CharField(max_length = 200)
    support_office = models.ForeignKey(SupportOffice, on_delete = models.CASCADE)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End Date')
    description = models.CharField(max_length = 200)
    grant_amount = models.IntegerField('Grant Amount')

    def __str__(self):
        return self.project_name

    def get_status(self):
        """Method determies the status of the project whether future, current, past"""
        if self.start_date <= timezone.now() <= self.end_date:
            return "Open"
        elif self.start_date < self.end_date < timezone.now():
            return "Closed"
        else:
            return "Upcoming"

    def get_donor(self):
        """"""
        pass

class Donor(models.Model):
    name = models.CharField(max_length = 200)
    physical_address = models.CharField(max_length = 200)
    email_address = models.CharField(max_length = 200)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.name



class Expenditure(models.Model):
    expenditure_text = models.CharField(max_length = 200)
    exp_date = models.DateTimeField('Date of Expenditure')
    amount_spent = models.IntegerField('Amount spent')
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.expenditure_text

class Payment(models.Model):
    payment_text = models.CharField(max_length = 200)
    pay_date = models.DateTimeField('Payment Date')
    amount_paid = models.IntegerField('Amount paid')
    project = models.ForeignKey(Project, on_delete = models.CASCADE )


    def __str__(self):
        return self.payment_text
