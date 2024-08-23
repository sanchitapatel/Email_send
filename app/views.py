from django.shortcuts import render
from django.http import HttpResponse
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail               # add this for single message
from django.core.mail import send_mass_mail         # add this for mass message

# Create your views here.
def home(request): 
    # send_mail(
    # "Test_Mail from Django",
    # "This is a test mail",
    # "neeraj.patel2505@gmail.com",
    # ["neeraj.patel2505@gmail.com","neerajkumar.javaventures@gmail.com"],
    # fail_silently=False,)
    # or
    
    subject="Test_Mail from Django Server"
    message="This is a Demo-test mail"
    from_email=EMAIL_HOST_USER
    recipient_list=["sanchita15pa@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)


    # or for mass mail..............................................
    # msg1=["Test_Mail from Django Server",
    #      "This is a Demo-test mail",
    #      "neeraj.patel2505@gmail.com",
    #      ["neeraj.patel2505@gmail.com","neerajkumar.javaventures@gmail.com","uikeyom1234@gmail.com","ghanshyamsharmaji24@gmail.com"]
    #     ]
    
    # msg2=["Test_Mail from Django Server-12345",
    #      "This is a Demo-test mail-12345",
    #      "neeraj.patel2505@gmail.com",
    #      ["neeraj.patel2505@gmail.com","neerajkumar.javaventures@gmail.com","uikeyom1234@gmail.com","ghanshyamsharmaji24@gmail.com"]
    #     ]
    # send_mass_mail((msg1, msg2), fail_silently=False)
    
    return HttpResponse("please check your new_email")
