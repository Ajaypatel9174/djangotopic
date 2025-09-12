from django.shortcuts import render,HttpResponse
from.serializer import Stu_Serializer
from app.models import Student
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def list(request):
    if request.method == 'POST':
        print("POST comes from vs-code")
        print(request.body)
        data = json.loads(request.body)
        print(data)
        print(type(data))
        Student.objects.create(stu_name=data['stu_name'],stu_email=data['stu_email'],stu_contact=data['stu_contact'],stu_image=data['stu_image'],stu_resume=data['stu_resume'])
        print('data save success')
        d={'msg': "data saved"}
        return JsonResponse(d)

    else:
        all_stu = Student.objects.all()
        serializer = Stu_Serializer(all_stu,many=True)
        # print(serializer)
        # print(serializer.data)
        # return JsonResponse(serializer.data,safe=False)
        J_data = json.dumps(serializer.data)
        print(J_data)
        return HttpResponse(J_data,content_type='application/Json')

    
@csrf_exempt
def detail(request,pk):
    
    # stu_data = Student.objects.get(id=pk)
    # serializer = Stu_Serializer(stu_data)
    # # print(serializer)
    # # print(serializer.data)
    # # print(type(serializer.data))
    # J_data = json.dumps(serializer.data)
    # print(J_data)
    # return HttpResponse(J_data, content_type='application/json')

    
    
    if request.method=='DELETE':
        # -------------send id through url
        # id = pk
        # data = Student.objects.get(id=id)
        # data.delete()
        # return JsonResponse({'msg':'object deleted'})

        # -------------send id through body
        json_data = request.body
        py_data = json.loads(json_data)
        id = py_data['id']
        data1 =Student.objects.filter(id=id)
        if not data1:
            return JsonResponse({'msg':'this id is not found in DataBase'})

        print(id)
        data = Student.objects.get(id=id)
        data.delete()
        return JsonResponse({'msg':'object deleted'})
    
    elif request.method=='PATCH':
        id = pk 
        data = Student.objects.get(id=id)
        p_data = json.loads(request.body)
        data.name = p_data['name']
        data.save()
        return JsonResponse({'msg':'Partial data update'})
    
    elif request.method=='PUT':
        id = pk 
        data = Student.objects.get(id=id)
        p_data = json.loads(request.body)
        data.name = p_data['name']
        data.save()
        return JsonResponse({'msg':'Partial data update'})


    stu_data = Student.objects.get(id=pk)
    serializer = Stu_Serializer(stu_data)
    # print(serializer)
    # print(serializer.data)
    # print(type(serializer.data))
    j_data = json.dumps(serializer.data)
    print(j_data)
    return HttpResponse(j_data, content_type='application/json')
    


    

