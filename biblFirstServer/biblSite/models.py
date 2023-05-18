from django.db import models


# Create your models here.
class AddressBook(models.Model):
    name = models.CharField(max_length=100)
    fam = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    note = models.CharField(max_length=100)

    objects = models.Manager()
