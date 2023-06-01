from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required

from users.models import Patient, Doctor, Caregiver





def hcamMain(request):
    return render(request, 'device.html')
def userMain(request):
    return render(request, 'about.html')



def adminPage(request):   
    context={}
    return render(request, 'hcam/adminPage.html', context)


@login_required(login_url="login")
def doctorPage(request):
    doctorObj = Doctor.objects.all()
    context = {'doctorObj': doctorObj}
    return render(request, 'hcam/doctorPage.html', context)

@login_required(login_url="login")
def caregiverPage(request):
    caregiverObj = Caregiver.objects.all()
    context = {'caregiverObj': caregiverObj}
    return render(request, 'hcam/caregiverPage.html', context)


@login_required(login_url="login")
def patientPage(request):
    patientObj = Patient.objects.all()

    context = {'patients':patientObj}
    return render(request, 'hcam/patientPage.html', context)

