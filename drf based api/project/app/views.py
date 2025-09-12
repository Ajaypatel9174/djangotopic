from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from.serializers import StudentSerializer
from.models import Student
import io
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

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
            return JsonResponse({'msg':'data saved'})
        else:
            JsonResponse(seralizer.errors)
       
    all_data = Student.objects.all()
    seralizer = StudentSerializer(all_data,many=True)
    print(seralizer.data)
    content = JSONRenderer().render(seralizer.data)
    print(content)
    return JsonResponse(seralizer.data,safe=False)
    

@csrf_exempt
def stu_detail(req,pk):
    if req.method=='PUT':
        data = req.body
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id=pk)
        serializer = StudentSerializer(old_data,data=p_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'data uplod'})
        else:
            return JsonResponse(serializer.errors)
        
    
    elif req.method=='PATCH':
        data = req.body
        stream = io.BytesIO(data)
        p_data = JSONParser().parse(stream)
        old_data = Student.objects.get(id=pk)
        serializer = StudentSerializer(old_data,data=p_data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'data uplod'})
        else:
            return JsonResponse(serializer.errors)


        # old_p_data= model_to_dict(old_data)
        # print(old_p_data)
        # old_p_data['name']=p_data['name']
        # old_p_data['email']=p_data['email']
        # old_p_data['contact']=p_data['contact']
        # print(old_p_data)
@csrf_exempt     
def Student(req):
    data = req.body
    p_data = JSONParser().parse(data)
    pk = p_data['id']

        
    

    if 'id' in p_data:
        pk = p_data['id']

        if req.method=='GET':
            data = Student.objects.get(id=pk)
            serializer = StudentSerializer(data)
            return JsonResponse(serializer.data)
    
        if req.method=='PUT':
            data = req.body   
            stream = io.BytesIO(data)
            p_data = JSONParser().parse(stream)
            old_data = Student.objects.get(id=pk)
            # old_p_data = model_to_dict(old_data)
            # print(old_p_data)
            # old_p_data['name'] = p_data['name']
            # old_p_data['email'] = p_data['email']
            # old_p_data['contact'] = p_data['contact']
            # print(old_p_data)
            serializer = StudentSerializer(old_data,data=p_data)#,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'data Updated'})
            else:
                return JsonResponse(serializer.errors)
        
        elif req.method=='PATCH':
            data = req.body   
            stream = io.BytesIO(data)
            p_data = JSONParser().parse(stream)
            old_data = Student.objects.get(id=pk)
            # old_p_data = model_to_dict(old_data)
            # print(old_p_data)
            # old_p_data['name'] = p_data['name']
            # old_p_data['email'] = p_data['email']
            # old_p_data['contact'] = p_data['contact']
            # print(old_p_data)
            serializer = StudentSerializer(old_data,data=p_data,partial=True)#,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'data Updated'})
            else:
                return JsonResponse(serializer.errors)
        

        elif req.method=='DELETE':
            data = Student.objects.get(id=pk)
            data.delete()
            return JsonResponse({'msg':'data Deleted'})
    
    else:
        if req.method=='GET':
            all_data = Student.objects.all()
            serializer = StudentSerializer(all_data,many=True)
            print(serializer.data)
            content = JSONRenderer().render(serializer.data)
            print(content)
            return JsonResponse(serializer.data,safe=False)
        
        if req.method=='POST':
            content = req.body
            print(content)
            stream = io.BytesIO(content)
            print(stream)
            pdata = JSONParser().parse(stream)
            print(pdata)
            serializer = StudentSerializer(data=pdata)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                return JsonResponse({"msg":"Data Saved"})
            else:
             return JsonResponse(serializer.errors)





    
