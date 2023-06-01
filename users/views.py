from django.shortcuts import render, redirect
from multiprocessing import context
from .models import UserAccount, Patient, Disease, Doctor, Caregiver
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import PatientForm, CaregiverForm, DiseaseForm, DoctorForm, RecommendationForm, PatientStatusForm, CustomUserCreationForm

# Create your views here.

# About the patient

def patients(request):
    patientObj = Patient.objects.all()
    diseases = Disease.objects.all()
    context = {'patients':patientObj, 'diseases':diseases}
    return render(request, 'users/patients.html', context)

def singlePatient(request, pk):
    singlePatientObject = Patient.objects.get(id=pk)
    diseases = Disease.objects.all()
    context = {'singlePatientObject':singlePatientObject, 'diseases':diseases}
    return render(request, 'users/single-patient.html', context)

def updatePatientForm(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient) 
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patients')
    
    context={'form': form }
    return render(request, 'users/patient-form.html', context)

def deletePatientForm(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')
    context={'object':patient}
    return render(request, 'users/delete-patient.html', context)


#About the doctor
def doctors(request):
    doctorObj = Doctor.objects.all()
    context = {'doctorObj': doctorObj}
    return render(request, 'users/doctors.html', context)

def singleDoctor(request, pk):
    singleDoctorObj = Doctor.objects.get(id=pk)
    context = {'singleDoctorObj': singleDoctorObj}
    return render(request, 'users/single-doctor.html', context)

def updateDoctorForm(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=doctor)
    
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
        return redirect('doctors')
    
    context={'form': form}
    return render(request, 'users/doctor-form.html', context)

def deleteDoctorForm(request, pk):
    doctor = Doctor.objects.get(id=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('patients')
    context={'object':doctor}
    return render(request, 'users/delete-doctor.html', context)



#About the caregiver
def caregivers(request):
    caregiverObj = Caregiver.objects.all()
    context = {'caregiverObj': caregiverObj}
    return render(request, 'users/caregivers.html', context)

def singleCaregiver(request, pk):
    singleCaregiverObj = Caregiver.objects.get(id=pk)
    context = {'singleCaregiverObj': singleCaregiverObj}
    return render(request, 'users/single-caregiver.html', context)

def updateCaregiverForm(request, pk):
    caregiver = Caregiver.objects.get(id=pk)
    form = CaregiverForm(instance=caregiver)
    
    if request.method == "POST":
        form = CaregiverForm(request.POST, request.FILES, instance=caregiver)
        if form.is_valid():
            form.save()
        return redirect('caregivers')
    
    context={'form': form}
    return render(request, 'users/caregiver-form.html', context)

def deleteCaregiverForm(request, pk):
    caregiver = Caregiver.objects.get(id=pk)
    if request.method == 'POST':
        caregiver.delete()
        return redirect('caregivers')
    context={'object':caregiver}
    return render(request, 'users/delete-caregiver.html', context)



#the device related
def recommendationForm(request):
    recform = RecommendationForm()
    context={'recform': recform}
    return render(request, 'users/recommendation-form.html', context)

def diseaseForm(request):
    disform = DiseaseForm()
    context={'disform': disform}
    return render(request, 'users/disease-form.html', context)

def patientStatusForm(request):
    statusForm = PatientStatusForm()
    context={'statusForm': statusForm}
    return render(request, 'users/status-form.html', context)




#Use Login
def loginRegister(request):   
    page = 'login'       
    # if request.user.is_authenticated:
    #     return redirect('hcam-main')       
    
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']               
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist! ")                            
        user = authenticate(request, username=username, password=password)

        if user is not None:   
            role = user.type       
            if role == 'DOCTOR':               
                login(request, user)
                return redirect('single-doctor', user.doctor.id) 
            elif role == 'PATIENT':
                login(request, user)
                return redirect('single-patient', user.patient.id) 
            elif role == 'CAREGIVER':
                login(request, user)
                return redirect('single-caregiver', user.caregiver.id)   
            else:                           
                login(request, user)
                return redirect('hcam-main')
        else:
            messages.error(request, "Username or password is incorrect! ")       
                        
    return render(request, 'users/login-register.html')


#User logout
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was succesfuly logged out!')
    return redirect('login')


#User registration
def registerUser(request):
    
    page = 'registerUser'  
     
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        role = request.POST['type']
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()                  

            if role == 'DOCTOR':
                return redirect('doctors' ) 
            elif role == 'PATIENT':
                return redirect('patients')
            elif role == 'CAREGIVER':
                return redirect('caregivers')   
            else:
                return redirect('hcam-main')        
                
    context={'page':page, 'form':form}
    return render(request, 'users/login-register.html', context)


#Return to doctor
def registerDoctor(request):
    page = 'registerDoctor'
    
    form = DoctorForm()
    
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()           
            messages.success(request, 'Doctor account was succesfuly created!  ')
        return redirect('doctors')
                     
    context={'page':page, 'form':form}
    return render(request, 'users/doctor-form.html', context)

#Return to Patient
def registerPatient(request):
    page = 'registerPatient'
    
    form = PatientForm()
    
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()           
            messages.success(request, 'Patient account was succesfuly created!  ')     
        return redirect('patients')        
                        
    context={'page':page, 'form':form}
    return render(request, 'users/patient-form.html', context)


# Return to Caregiver
def registerCaregiver(request):
    page = 'registerCaregiver'
    
    form = CaregiverForm()
    
    if request.method == "POST":
        form = CaregiverForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()           
            messages.success(request, 'Caregiver account was succesfuly created!  ')
        return redirect('caregivers')
                
    context={'page':page, 'form':form}
    return render(request, 'users/caregiver-form.html', context)



def doctorForm(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('doctors')
    context={'form':form}
    return render(request, 'users/doctor-form.html', context)

def caregiverForm(request):
    form = CaregiverForm()
    if request.method == 'POST':
        form = CaregiverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('caregivers')
    context={'form':form}
    return render(request, 'users/caregiver-form.html', context)

def patientForm(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('patients')
    context={'form':form}
    return render(request, 'users/patient-form.html', context)



##################

def editPatientProfile(request):
    user = User.objects.get(id=request.user.id)
    patient = user.patient
    form = PatientForm(instance=patient)
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('patients')
    
    context={'form': form}
    return render(request, 'users/edit-patient-profile.html', context)