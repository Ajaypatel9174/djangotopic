from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField()
    contact = models.IntegerField()
    image = models.ImageField(upload_to='image/')
    resume = models.FileField(upload_to='document/')
