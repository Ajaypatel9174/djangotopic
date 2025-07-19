from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'home.html',{'register':'register'})

def registerdata(request):
    print('hello....')
    print(request.method)
    print(request.POST)
    print(request.FILES)

    if request.method=='POST':
        n=request.POST.get('name')
        e=request.POST.get('email')
        c=request.POST.get('contact')
        i=request.FILES.get('image')
        r=request.FILES.get('resume')
        print(n,e,c,i,r,sep=',')


        Student.objects.create(stu_name=n,stu_email=e,stu_contact=c,stu_image=i,stu_resume=r)
        msg='registration done'
        return render(request,'home.html',{'msg':msg})