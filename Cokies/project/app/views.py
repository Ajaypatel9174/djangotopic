from django.shortcuts import render,HttpResponse


# Create your views here.

def landing(req):
    # return render(req,'landing.html')
    print("hello")
    print(req.COOKIES)
    data = HttpResponse('landing.html')
    
    data.set_cookie('key','Ajay')
    data.set_cookie('email','a@gmail.com')
    return data

    

