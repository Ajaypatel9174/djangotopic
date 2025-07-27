from django.shortcuts import render
from .models import Student
from .models import Query1


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
def login(request):
        if request.method == 'POST':
            e = request.POST.get('email')
            p = request.POST.get('password')
            data = Student.objects.filter(stu_email=e)
            print(e,p,data)
            if data:
                user = Student.objects.get(stu_email=e)
                password = user.stu_password

                if password == p:
                    data={'name':user.stu_name,
                          'email':user.stu_email,
                          'contact':user.stu_contact,
                          'password':user.stu_password,
                          'image':user.stu_image,
                          'id':user.id}
                    return render(request,'dasboard.html',{'data':data})
                else:
                    msg = "password not matched"
                    return render(request,'login.html',{'email':e})
            else:
                msg = "Email id not register"
                return render(request,'home.html',{'msg':msg})             
        else:
            return render(request,'login.html')
    
def query(request,pk):
    user = Student.objects.get(id=pk)
    data={'name':user.stu_name,
          'email':user.stu_email,
          'contact':user.stu_contact,
          'password':user.stu_password,
          'image':user.stu_image,
          'id':user.id,}
        #   'query':'query'}
    return render(request,'dasboard.html',{'data':data,'query':'query'})
   
def querydata(request):
    if request.method=='POST':
        e = request.POST.get('email')                       
        n = request.POST.get('name')                       
        q = request.POST.get('query')
        Query1.objects.create(stu_name=n,stu_email=e,stu_query=q)   
        user = Student.objects.get(stu_email=e)
        data={'name':user.stu_name,
            'email':user.stu_email,
            'contact':user.stu_contact,
            'password':user.stu_password,
            'image':user.stu_image,
            'id':user.id,}
        return render(request,'dasboard.html',{'data':data})
    


        # Student.objects.create(stu_name=n,stu_email=e,stu_contact=c,stu_image=i,stu_resume=r)
        # msg='registration done'
        # return render(request,'home.html',{'msg':msg})