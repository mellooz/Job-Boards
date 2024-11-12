from django.conf import settings
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
# Create your views here.


def send_message(request):
    myinfo = Info.objects.first()
    if request.method == 'POST' :
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "from@example.com",
        #     ["to@example.com"],
        # )
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request , 'contact/contact.html' , {'myinfo' : myinfo})
