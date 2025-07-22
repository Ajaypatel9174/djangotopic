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
        p=request.POST.get('password')
        cp=request.POST.get('cpassword')
        print(n,e,c,i,r,p,cp,sep=',')

        data=Student.objects.filter(stu_email=e)
        if data:
            msg="Email already exist"
            return render(request,'home.html',{'msg':msg})
        
        else:
            if p==cp:
                Student.objects.create(stu_name=n,stu_email=e,stu_contact=c,stu_image=i,stu_resume=r,stu_password=p,stu_cpassword=cp)
                msg="Resigtration succesfull"
                return render(request,'login.html',{'msg':msg})
            
            else:
                msg = "password $ cpassword not matched"
                return render(request,'home.html',{'msg':msg,'name':n,'email':e,'contact':c,'image':i,'resume':r,'password':p,'cpassword':cp})


        Student.objects.create(stu_name=n,stu_email=e,stu_contact=c,stu_image=i,stu_resume=r)
        msg='registration done'
        return render(request,'home.html',{'msg':msg})