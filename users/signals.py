from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Patient, Doctor, Caregiver
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


def createUserProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        if user.type == "DOCTOR":
            doctor = Doctor.objects.create(
                user = user,
                username = user.username,
                email = user.email,
                first_name = user.first_name,
                
                #middle_name = user.last_name,
                
                            
            )      
            # doctor = Doctor.objects.create(
            #     doctor=doctor,           
            # )   
            
        elif user.type == "PATIENT":
            patient = Patient.objects.create(
                user = user,
                username = user.username,  
                first_name = user.first_name,
                #middle_name = user.last_name,
                email = user.email,
                          
            )      
            # patient = Patient.objects.create(
            #     patient=patient,           
            # )
        
        else:
            caregiver = Caregiver.objects.create(
                user = user,
                username = user.username, 
                first_name = user.first_name,
                email = user.email,
                #middle_name = user.last_name,
                
                           
            )      
            # caregiver = Caregiver.objects.create(
            #     caregiver=caregiver,           
            # )
       

def updateDoctor(sender, instance, created, **kwargs):
    doctor = instance
    user = doctor.user
    
    if created == False:
        user.first_name = doctor.first_name
        user.username = doctor.username
        user.email = doctor.email
        user.save() 
        
def updatePatient(sender, instance, created, **kwargs):
    patient = instance
    user = patient.user
    
    if created == False:
        user.first_name = patient.first_name
        user.username = patient.username
        user.email = patient.email
        user.save() 

def updateCaregiver(sender, instance, created, **kwargs):
    caregiver = instance
    user = caregiver.user
    
    if created == False:
        user.first_name = caregiver.first_name
        user.username = caregiver.username
        user.email = caregiver.email
        user.save() 
        
     
     
           
               
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete() 
    except:
        pass      
                   



post_save.connect(createUserProfile, sender=User)

post_save.connect(updateDoctor, sender=Doctor)
post_save.connect(updatePatient, sender=Patient)
post_save.connect(updateCaregiver, sender=Caregiver)

post_delete.connect(deleteUser, sender=Doctor)
post_delete.connect(deleteUser, sender=Patient)
post_delete.connect(deleteUser, sender=Caregiver)




############commented##########
"""
@receiver(post_save, sender=Doctor)
def updateDoctor(sender, instance, created, **kwargs):
    print("Doctor updated")
"""  
    