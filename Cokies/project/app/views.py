from django.shortcuts import render,HttpResponse


# Create your views here.

def landing(req):
    return render(req,'landing.html')
    # print("hello")
    # print(req.COOKIES)
    
    # data = HttpResponse('landing.html')
    
    # data.set_cookie('key','Ajay')
    # data.set_cookie('email','a@gmail.com')
    # return data

def register(req):
    if req.method == 'POST':
        response = render(req,'login.html')
        response.set_cookie('name',req.POST.get('name'))
        response.set_cookie('name',req.POST.get('email'))
        response.set_cookie('name',req.POST.get('contact'))
        response.set_cookie('name',req.POST.get('password'))

    return render(req,'register.html')


def login(req):
    if req.method=='POST':
        if req.POST.get('email')==req.COOKIES.get('email'):

            if req.POST.get('password')==req.COOKIES.get('password'):
                n = req.POST.get('name')
                e = req.POST.get('email')
                c = req.POST.get('contact')
                p = req.POST.get('password')

                data = {'n':n,'e':e,'c':c,'p':p}
                return render(req,'dashboard.html',{'data':data})
            
            else:
                msg = 'email not register'
                return render(req,'login.html',{'msg':msg})
    
                
                
            
                
        
    



    

