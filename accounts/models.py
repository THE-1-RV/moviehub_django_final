from django.db import models
from django.utils.timezone import now

class Login(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    cnf_password = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.username} - {self.email}"

class Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.email}"

class Search(models.Model):
    sno = models.AutoField(primary_key=True)
    movie = models.CharField(max_length=150)
    date_searched = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.movie} - {self.date_searched}"
