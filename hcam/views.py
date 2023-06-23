from django.shortcuts import render
# Create your views here.
from django.contrib.auth.decorators import login_required

from users.models import Patient, Doctor, Caregiver, Hospital




def hcamMain(request):
    hospital = Hospital.objects.get(id = "44a01626-5ce1-42e3-ba97-d82a95d377c3")
    context = {'hospital': hospital}
    return render(request, 'device.html', context)


def userMain(request):
    hospital = Hospital.objects.get(id="44a01626-5ce1-42e3-ba97-d82a95d377c3")
    context = {'hospital': hospital}
    return render(request, 'about.html', context)


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

