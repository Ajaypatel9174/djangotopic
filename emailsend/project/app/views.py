from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail


# Create your views here.
def home(req):
    return render(req,'home.html')

def sendmail(req):
    if req.method == 'POST':
        sub = req.POST.get('subjects')
        msg = req.POST.get('msg')
        frrom = req.POST.get('email')
        to = ["ajaypatelgurjar01@gmail.com"]
        send_mail(sub,msg,frrom,to,fail_silently=False)
        return HttpResponse("mail send succesfull")
    
# send_mail(
#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,
# )

