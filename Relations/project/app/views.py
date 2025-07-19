from django.shortcuts import render
from .models import Student
from .models import Adhar
from .models import Student1
from .models import Department


# Create your views here.

# def fa(request):
#     stu_data=Student.objects.get(id=1)
#     print(stu_data.name)
#     print(stu_data.email)
#     print(stu_data.contact)
#     print(stu_data.adharnumber)
#     print(stu_data.adharnumber.adharnumber)
#     print(stu_data.adharnumber.created_by)
#     print(stu_data.adharnumber.created_date)


def ra(request):
    a_data=Adhar.objects.get(id=1)

    print(a_data.adharnumber)
    print(a_data.created_by)
    print(a_data.created_date)
    print(a_data.StudentInfo)
    print(a_data.StudentInfo.name)
    print(a_data.StudentInfo.contact)
    print(a_data.StudentInfo.email)

    
    def fa(request):
        stu_data=Student1.objects.get(id=1)
        print(stu_data.name)
        print(stu_data.email)
        print(stu_data.contact)
        print(stu_data.d_name)
        print(stu_data.d_name.d_name)



def ra(request):
     dep=Department.objects.get(d_name='ECE')
     all_stu = dep.StudentInfo.all()

     print(all_stu)

     for i in all_stu:
         print(i)




     
     
