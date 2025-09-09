from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from.serializers import StudentSerializer
from.models import Student
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def stu_list(req):
    if req.method=='POST':
        content = req.body
        print(content)
       

        stream = io.BytesIO(content)
        print(stream)
        pdata = JSONParser().parse(stream)
        print(pdata)
        seralizer = StudentSerializer(data=pdata)
        if seralizer.is_valid():
            print(seralizer.validated_data)
            seralizer.save()
        else:
            JsonResponse(seralizer.errors)
       
    all_data = Student.objects.all()
    seralizer = StudentSerializer(all_data,many=True)
    print(seralizer.data)
    content = JSONRenderer().render(seralizer.data)
    print(content)
    return JsonResponse(seralizer.data,safe=False)
    


def stu_detail(req,pk):

    pass
