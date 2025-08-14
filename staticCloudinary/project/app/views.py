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


def MediaData(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        i = request.P.get('image')
        d = request.POST.get('document')
        v = request.POST.get('vidio')
        a = request.POST.get('audio')
        print(n,i,d,v,a)
