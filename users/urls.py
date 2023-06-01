from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients, name = 'patients'),
    path('single-patient/<str:pk>/', views.singlePatient, name = 'single-patient'),
    path('update-patient/<str:pk>/', views.updatePatientForm, name = 'update-patient'),
    path('delete-patient/<str:pk>/', views.deletePatientForm, name = 'delete-patient'),
    
    
    path('doctors/', views.doctors, name = 'doctors'),
    path('single-doctor/<str:pk>/', views.singleDoctor, name = 'single-doctor'),
    path('update-doctor/<str:pk>/', views.updateDoctorForm, name = 'update-doctor'),
    path('delete-doctor/<str:pk>/', views.deleteDoctorForm, name = 'delete-doctor'),
    
    path('caregivers/', views.caregivers, name = 'caregivers'),
    path('single-caregiver/<str:pk>/', views.singleCaregiver, name = 'single-caregiver'),
    path('update-caregiver/<str:pk>/', views.updateCaregiverForm, name = 'update-caregiver'),
    path('delete-caregiver/<str:pk>/', views.deleteCaregiverForm, name = 'delete-caregiver'),
    
    path('register-doctor/', views.registerDoctor, name='register-doctor'),
    path('register-patient/', views.registerPatient, name='register-patient'),
    path('register-caregiver/', views.registerCaregiver, name='register-caregiver'),
    
    # path('doctor-form/', views.doctorForm, name = 'doctor-form'),
    # path('patient-form/', views.patientForm, name = 'patient-form'),
    # path('caregiver-form/', views.caregiverForm, name = 'caregiver-form'),
    
    path('edit-patient-profile/', views.editPatientProfile, name = 'edit-patient-profile'),
    # path('doctor-profile-form/', views.doctorProfileForm, name = 'doctor-profile-form'),
    # path('caregiver-profile-form/', views.caregiverProfileForm, name = 'caregiver-profile-form'),  
    
    path('register-disease/', views.diseaseForm, name = 'register-disease'),
    

    path('status-form/', views.patientStatusForm, name = 'status-form'),
    path('give-recommendation/', views.recommendationForm, name = 'give-recommendation'),
    
    
    path('login/', views.loginRegister, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    
]

