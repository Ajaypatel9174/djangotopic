from django.db import models

# Create your models here.

class Employ(models.Model):
    e_name=models.CharField(max_length=50)
    e_email=models.EmailField()
    e_city=models.CharField()
    e_contact=models.IntegerField()


