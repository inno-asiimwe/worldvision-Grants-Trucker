from django.db import models

# Create your models here.
class Donor(models.Model):
    name = models.CharField(max_length = 200)
    physical_address = models.CharField(max_length)
    email_address = models.CharField(max_length)

    def __str__(self):
        return self.name

class SupportOffice(models.Model):
    name = 
