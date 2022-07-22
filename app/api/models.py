from django.db import models
# Create your models here.


class User(models.Model):
  firstName = models.CharField(max_length=10, default="")
  lastName = models.CharField(max_length=10, default="")
  username = models.CharField(max_length=10, default="", unique=True)
  password = models.CharField(max_length=10, default="")
  login_loc = models.CharField(max_length=140, default="", unique=True)
  login_time = models.IntegerField(null=False, default=1)

  

  

