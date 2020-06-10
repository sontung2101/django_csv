from django.db import models


# Create your models here.
class MyUser(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
