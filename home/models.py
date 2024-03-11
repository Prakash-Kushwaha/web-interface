from django.db import models

# Create your models here.
class Persons(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name + self.age + self.gender + self.email + self.password