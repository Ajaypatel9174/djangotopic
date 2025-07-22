from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name=models.CharField(max_length=70)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_image=models.ImageField(upload_to='image/')
    stu_resume=models.FileField(upload_to='resume/')
    stu_password=models.CharField(max_length=50)
    stu_cpassword=models.CharField(max_length=50)