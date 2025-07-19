from django.shortcuts import render

# Create your views here.

def landing(req):
    return render(req,'landing.html')


def register(req):
    return render(req,'landing.html',{'register':'register'})

def registerdata(req):
    print("hello...")
    print(req.method)
    print(req.POST)
    print(req.FILES)
    # if req.method=='POST':
    #     n=req.POST.get('name')
    #     e=req.POST.get('name')
    #     c=req.POST.get('name')
    #     i=req.FILES.get('name')
    #     d=req.FILES.get('name')

        # Student.object.create(nmae=n,email=e,contact=c,image=i,document=d)
        # msg="resistration data saved"
        # return render(req,'lannding.html',{'msg':msg})