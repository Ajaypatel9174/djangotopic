from django.shortcuts import render
from .forms import stuform

# Create your views here.

def landing(request):
    return render(request,'landing.html')

def landing(request):
    if request.method=='POST':
        form=stuform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form=stuform()
            return render(request,'landing.html',{'frm':form})

    form = stuform()
    return render(request,'landing.html',{'frm':form})
