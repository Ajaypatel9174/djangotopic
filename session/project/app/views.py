from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')

def dashboard(req):
    if 'email' in req.session:
        return render(req,'dashboard.html')
    return render(req,'login.html')

def register(req):
     if req.method == 'POST':

         n = req.POST.get('name')
         e = req.POST.get('email')
         c = req.POST.get('contact')
         d = req.POST.get('document')
         p = req.POST.get('password')

         req.session['name']= n
         req.session['email']= e
         req.session['contact']= c
         req.session['document']= d
         req.session['password']= p

         return render(req,'login.html')
     return render(req,'register.html')


def login(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        
        e = req.session.get('email')
        p = req.session.get('password')

        
        print(e)
        print(p)

        if email == e:
            if password == p:
                msg = 'login susecfull'
                return render(req,'dashboard.html',{'msg':msg})
            else:
                msg = 'password not matched'
                return render(req,'login.html',{'msg':msg})

        else:
            msg = 'user not found'        
            return render(req,'login.html',{'msg':msg})

    return render(req,'login.html')

def logout(req):
    print(req.session)
    if 'email' in req.session:
        req.session.flush()
        return render(req,'login.html')
    


