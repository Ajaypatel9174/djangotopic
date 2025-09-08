from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from.serializers import StudentSerializer
from.models import Student

# Create your views here.

def stu_list(req):
    all_data = Student.objects.all()
    seralizer = StudentSerializer(all_data,many=True)
    print(seralizer.data)
    content = JSONRenderer().render(seralizer.data)
    print(content)
    return JsonResponse(seralizer.data,safe=False)
    


def stu_detail(req,pk):
    pass
