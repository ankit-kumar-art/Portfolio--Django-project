from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()
    def __str__(self):
     return self.name
