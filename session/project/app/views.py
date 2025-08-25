from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')

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

         return render(req,'register.html')
     return render(req,'register.html')


def login(req):
    return render('login.html')


    


