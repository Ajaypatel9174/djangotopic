from django.shortcuts import render,HttpResponse
from.serializer import Stu_Serializer
from app.models import Student
from django.http import JsonResponse
import json


# Create your views here.
def list(request):
    all_stu = Student.objects.all()
    serializer = Stu_Serializer(all_stu,many=True)
    # print(serializer)
    # print(serializer.data)
    # return JsonResponse(serializer.data,safe=False)
    J_data = json.dumps(serializer.data)
    print(J_data)
    return HttpResponse(J_data,content_type='application/Json')

    

def detail(request):
    # stu_data =Student.objects.get(id=pk)
    pass


    
