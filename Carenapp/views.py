from django.shortcuts import render
from django.core.mail import send_mail
# from django.contrib.auth.form import usercreationform

# Create your views here.
def home(request):
    return render(request,'home.html',{})
def about(request):
    return render(request,'about.html',{})

def services(request):
    return render(request, 'services.html',{}) 
def nutritionist(request):
    return render(request, 'nutritionist.html',{}) 

def training(request):
    return render(request, 'training.html',{})
def register(request):
    return render(request, 'register.html',{})    
def login(request): 
    return render(request, 'login.html',{})
def logout(request):
    return render(request,'logout.html',{})
                  
          

def contact(request):
    if request.method=='POST':
        Message_name = request.POST[" Message + name"]
        Message_email=request.POST[" Message + email"]
        Message_Subject=request.POST[" Message + subject"]
        umessage=request.POST[" umessage"]

        send_email(
              Message_name,#users name
              Message_Subject,# message subject
              umessage,# messages
              Message_email, #to email
              ["carenakhonya22@gmail.com"] # to email

        )
           
        return render(request,'contact.html',{" Message_name": Message_name})

    else:
            return render(request,'contact.html',{})