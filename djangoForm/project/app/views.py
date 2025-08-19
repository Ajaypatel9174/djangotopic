from django.shortcuts import render
from app.forms import Registrationform
from .models import Student

# Create your views here.

def resigster(request):
    if request.method == 'POST':

        form = Registrationform(request.POST,request.FILES)
        if form.is_valid():
            # form.save()
            # name = request.POST.get('name')
            # email = request.POST.get('email')
            # contact = request.POST.get('contact')
            # image = request.FILES.get('image')
            # resume = request.FILES.get('resume')
            # n = form.cleaned_data['name']
            # e = form.cleaned_data['email']
            # c = form.cleaned_data['contact']
            # i= form.cleaned_data['image']
            # r = form.cleaned_data['resume']
            # print(n,e,c,i,r)
            # Student.objects.create(name=n,email=e,contact=c,image=i,resume=r)
            form.save()
            return render(request,'register.html')
        return render(request,'register.html',{'fm':form})
    form = Registrationform()
    return render(request,'register.html',{'fm':form})

def landing(request):
    return render(request,'landing.html')