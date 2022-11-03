from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)   # input type text
    password = models.CharField(max_length=100)     # j.w.
    email = models.EmailField(max_length=100, null=True, blank=True)     # input type email

    def __str__(self):
        return self.username


class UserDetail(models.Model):
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username


