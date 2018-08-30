from django.db import models


# Food Model
class Food(models.Model):
    # Fields
    name = models.CharField(max_length=50)

    # Methods
    def __str__(self):
        return self.name


# Owner Model
class Owner(models.Model):
    # Fields
    name = models.CharField(max_length=50)
    passport = models.CharField(max_length=10)

    # Methods
    def __str__(self):
        return self.name


# Pet Model
class Pet(models.Model):
    # Fields
    name = models.CharField(max_length=50)
    date_in = models.DateField(auto_now_add=True)

    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)

    # Methods
    def __str__(self):
        return self.name
