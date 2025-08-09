from django.shortcuts import render ,redirect
from .models import Student
from .models import Query1
from django.urls import reverse
from urllib.parse import urlencode



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
                # return redirect(request,'login')
                url = reverse('login')
                qs = urlencode({'id':Student.id})
                return redirect(f'{url}?{qs}')
                
            
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
                    
                    url = reverse('dashboard')
                    # data1 = urlencode({'id':user.id})
                    request.session['id']=user.id
                    # return render(request,'dasboard.html',{'data':data})
                    # return redirect(f'{url}?{data1}')
                    return redirect(f'{url}')
                else:
                    msg = "password not matched"
                    return render(request,'login.html',{'email':e})
            else:
                msg = "Email id not register"
                return render(request,'home.html',{'msg':msg})             
        else:
            return render(request,'login.html')
    
def dashboard(request):
    # user_id = request.GET.get('id')
    user_id = request.session['id']
    user = Student.objects.get(id=user_id)
    data={'name':user.stu_name,
                          'email':user.stu_email,
                          'contact':user.stu_contact,
                          'password':user.stu_password,
                          'image':user.stu_image,
                          'id':user.id}
    return render(request, 'dasboard.html',{'data':data})
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
    
def  showquery(request,pk):
    user = Student.objects.get(id=pk)
    e = user.stu_email
    print(e)
    
    all_query = Query1.objects.filter(stu_email=e)

    data = {'name':user.stu_name,
            'email':user.stu_email,
            'contact':user.stu_contact,
            'password':user.stu_password,
            'image':user.stu_image,
            'id':user.id}
    return render(request,'dasboard.html',{'data':data,'all_query':all_query})
    
    
    
def edit(request,pk,pke):
    user = Student.objects.get(id=pk)
    data={'name':user.stu_name,
            'email':user.stu_email,
            'contact':user.stu_contact,
            'password':user.stu_password,
            'image':user.stu_image,
            'id':user.id}
    olddata=Query1.objects.get(id=pke)

    return render(request,'dasboard.html',{'data':data,'olddata':olddata})

    
def update(request,pk,pke):

    user = Student.objects.get(id=pk)
    data = {'name':user.stu_name,
            'email':user.stu_email,
            'contact':user.stu_contact,
            'password':user.stu_password,
            'image':user.stu_image,
            'id':user.id}


    olddata=Query1.objects.get(id=pke)
    if request.method=="POST":
 
        n = request.POST.get('name')         
        e = request.POST.get('email')                
        q = request.POST.get('query')

    # olddata.stu_query = request.POST.get('stu_query')
    olddata.stu_query=q
    olddata.save()

    all_query = Query1.objects.filter(stu_email=e)

    return render(request,'dasboard.html',{'data':data,'all_query':all_query})

def delete(request,pk,pke):
    querydata = Query1.objects.filter(id=pke)
    if querydata:
        deletequery = Query1.objects.get(id=pke)
       
        deletequery.delete()
        user = Student.objects.get(id=pk)
        e = user.stu_email
        all_query = Query1.objects.filter(stu_email=e)

        data = {'name':user.stu_name,
                'email':user.stu_email,
                'contact':user.stu_contact,
                'password':user.stu_password,
                'image':user.stu_image,
                'id':user.id}
        return render(request,'dasboard.html',{'data':data,'all_query':all_query})
    else:
        user = Student.objects.get(id=pk)
        data =  {'name':user.stu_name,
            'email':user.stu_email,
            'contact':user.stu_contact,
            'password':user.stu_password,
            'image':user.stu_image,
             'id':user.id}
        all_query=Query1.objects.filter(stu_email=user.stu_email)
        return render(request,'dasboard.html',{'data':data,'allquery':all_query})
    

def logout(request):
    request.session.flush()
    return redirect('login')

def Search(request):
    if request.method == 'POST':
        sv = request.POST.get('search')
        pk = request.session['id']
        user = Student.objects.get(id=pk)
        data = {'name':user.stu_name,
                'email':user.stu_email,
                'contact':user.stu_contact,
                'password':user.stu_password,
                'image':user.stu_image,
                'id':user.id}
        if sv:
            all_query = Query1.objects.filter(
            
            stu_query__icontains=sv,
                
            )
            return render(request,'dasboard.html',{'data':data,'all_query':all_query})
        else:
            all_query = Query1.objects.filter(stu_email=user.stu_email)
            return render(request,'dasboard.html',{'data':data,'all_query':all_query})


    
                 


    







    







    
    
    
    

    
    


 
    


        # Student.objects.create(stu_name=n,stu_email=e,stu_contact=c,stu_image=i,stu_resume=r)
        # msg='registration done'
        # return render(request,'home.html',{'msg':msg})