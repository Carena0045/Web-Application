from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.core.mail import send_mail
from .models import Appointment
from django.views.generic import ListView
import datetime
import imaplib
from django.template import Context
from django.template.loader import render_to_string, get_template
# from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request,'index.html',{})
def makeappointment(request):
    return render(request,'makeappointment.html',{})   
def about(request):
    return render(request,'about.html',{})
def patientviewappointments(request):
    return render(request,' patientviewappointments.html',{})
def services(request):
    return render(request, 'services.html',{}) 
def nutritionist(request):
    return render(request, 'nutritionist.html',{})
def doctorviewappointment(request):
    return render(request, 'doctorviewappointment.html',{})
def adminviewappointments(request):
    return render(request, 'adminviewappointments.html',{})    
def adminviewDoctors(request):
    return render(request, 'adminviewDoctors.html',{})
def adminaddreceptionist(request):
    return render(request, 'adminaddreceptionist.html',{})    
def adminadddoctor(request):
    return render(request, 'adminadddoctor.html',{})              
def profile(request):
    return render(request,'profile.html',{})
def makeappointment(request):
    return render(request, 'makeappointment.html',{})      
        
def training(request):
    return render(request, 'training.html',{})
def register(request):
    if request.method == "POST":
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleared_data.get('username')
            message.success(request, f'Hi, { username}, your account was successfully created')
            return redirect ('register/home')
        else:
            form =  UserRegisterForm()
        return render(request,'register.html',{'form': form})
        return render(request, "login.html", {'form': form})
        # return render(request, "register/index.html", {'form': form})
        # return response

           
      

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

class makeappointmentTemplateView(TemplateView):
    template_name = "makeappointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = makeappointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)

class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context            
class patienthomeView(TemplateView):
    template_name = "patienthome.html"
class doctorviewappointment(TemplateView):
    template_name = "doctorviewappointment.html"    
  
          