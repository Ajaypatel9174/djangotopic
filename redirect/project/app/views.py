from django.shortcuts import render,redirect
from django.urls import reverse


# Create your views here.
# def home(request):
#     # call internal url.s

#     return redirect("redirect1" , name='ajay',age=24)

# def redirect1(request,name,age):
#     return render(request,'redirect.html',{'x':name ,'y':age})



def home(request):
    url=reverse('redirect2',kwargs={'name':'Python','age':25})
    return redirect(url)

def redirect2(request,name,age):
    return render(request,'redirect2.html',{'x':name,'y':age})

