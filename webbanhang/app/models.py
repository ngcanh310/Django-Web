from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create form register
class CreateUser(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=200)
    rate = models.FloatField()

    def __str__(self):
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length=200)
    rate = models.FloatField()
    duration = models.CharField(max_length=200)

    def __str__(self) :
        return self.name
    
class Special(models.Model):
    name = models.CharField( max_length=200)
    duration = models.CharField(max_length = 200)

    def __str__(self) :
        return self.name