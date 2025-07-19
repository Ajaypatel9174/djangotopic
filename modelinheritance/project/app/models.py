from django.db import models

# Create your models here.


class Common(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    dob=models.DateField()
    class Meta:
        abstract=True



class Student(Common):
    branch=models.CharField(max_length=50)
    fees=models.IntegerField()

class Faculty(Common):
    dob=None
    salary=models.IntegerField()
    department=models.CharField(max_length=50)

    class Meta:
        db_table="faculty"

# multitabale inheritance
class A(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    dob=models.DateField()
    



class B(A):
    branch=models.CharField(max_length=50)
    fees=models.IntegerField()

class C(A):
    dob=None
    salary=models.IntegerField()
    department=models.CharField(max_length=50)

    class Meta:
        db_table="C"


class Real(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    dob=models.DateField()

class Proxy123(Real):
    class Meta:
        proxy=True

