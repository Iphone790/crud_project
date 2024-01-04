from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=200)
    esal = models.FloatField()
    eaddress = models.CharField(max_length=200)




