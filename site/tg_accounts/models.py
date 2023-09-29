from django.db import models


class RequiredUserModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

class UsernameModel(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    server = models.CharField(blank=True, max_length=50)
    text = models.TextField(blank=True, max_length=500) 
    status = models.BooleanField(default=False)
    start = models.DateTimeField(blank=True, null=True)

class SpammUsersModel(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    