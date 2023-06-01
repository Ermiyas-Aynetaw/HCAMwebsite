from django.urls import path
from . import views

urlpatterns = [
    path('', views.hcamMain, name = 'hcam-main'),
    path('about/', views.userMain, name = 'about'),
    path('admin-page/', views.adminPage, name = 'admin-page'),
    path('doctor-page/', views.doctorPage, name = 'doctor-page'),
    path('caregiver-page/', views.caregiverPage, name = 'caregiver-page'),
    path('patient-page/', views.patientPage, name = 'patient-page'),
]
