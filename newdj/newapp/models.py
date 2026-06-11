from django.db import models

# Create your models here.
class Employee(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Mobile = models.BigIntegerField()

    def __str__(self):
        return self.Firstname