from django.db import models

# Create your models here.
class Student(models.Model):

    contact = models.IntegerField()
    image = models.ImageField(upload_to='image/')
    resume = models.FileField(upload_to='document/')


