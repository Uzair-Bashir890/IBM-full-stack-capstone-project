from django.db import models
from django.contrib.auth.models import User


class CarMake(models.Model):
name = models.CharField(max_length=100)
def __str__(self): return self.name


class CarModel(models.Model):
make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
name = models.CharField(max_length=100)
def __str__(self): return f"{self.make.name} {self.name}"


class Dealer(models.Model):
external_id = models.IntegerField(null=True, blank=True)
name = models.CharField(max_length=200)
city = models.CharField(max_length=100)
state = models.CharField(max_length=50)
address = models.CharField(max_length=300, blank=True)
def __str__(self): return self.name


class Review(models.Model):
dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
content = models.TextField()
sentiment = models.CharField(max_length=50, blank=True)
created_at = models.DateTimeField(auto_now_add=True)