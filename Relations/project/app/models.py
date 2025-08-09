from django.db import models

# Create your models here.
class Adhar(models.Model):
    adharnumber =models.IntegerField()
    created_by =models.CharField()
    created_date=models.DateField()

    class Meta:
        db_table='Adhar'
        verbose_name_plural = 'Adhar'



class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    adharnumber=models.OneToOneField(Adhar,on_delete=models.PROTECT,related_name='StudentInfo')
   
class Department(models.Model):
    d_name =models.CharField(max_length=50)


class Student1(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    d_name =models.ForeignKey(Department,on_delete=models.PROTECT,related_name='StudentInfo')

class fuel(models.Model):
    fuel_name=models.CharField(max_length=50,unique=True)

class vehical(models.Model):
    v_name =models.CharField(max_length=50,unique=True)
    fuel_name=models.ManyToManyField(fuel,related_name='vehical')


