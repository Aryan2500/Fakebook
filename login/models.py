from django.db import models

# Create your models here.
class UserDetail(models.Model):
    emailOrPhone = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
