from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')[:6]
    coordinators = Coordinator.objects.all().order_by('-to_date')[:6]

    if request.method == "POST":
        subject = request.POST['subject']
        name = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        if name != "" and email != "" and subject != "":
            message = message + '\n\nFrom :- ' + email + '\n' + name
            send_mail(subject, message, email, ['alankrit.iiitg@gmail.com'])
    
    return render(request, 'index.html', {'posts': posts, 'coordinators': coordinators})
