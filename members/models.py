from django.db import models
# from django.utils import timezone
import datetime
# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joinDate = models.DateField(null = True)