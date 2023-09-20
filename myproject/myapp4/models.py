from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Age: {self.age}'

# Create your models here.
