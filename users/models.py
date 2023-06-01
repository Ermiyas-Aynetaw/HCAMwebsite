from django.db import models

from hcam.models import Hospital
from django.contrib.auth.models import AbstractUser
import uuid



# Create your models here.
class UserAccount(AbstractUser):
    Role = [  
        ("ADMIN", "Admin"),
        ("DOCTOR" , "Doctor"),
        ("PATIENT" , "Patient"),
        ("CAREGIVER", "Caregiver"),     
        ]
       
    type = models.CharField(max_length = 50 , choices = Role)  
    
    def create_superuser(cls, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return cls._create_user(username, email, password, **extra_fields)
      
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length = 200 , unique = True)
    first_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    

  
    def __str__(self):
        return str(self.username)
    
    def has_perm(self , perm, obj = None):
        return self.is_admin 
    
    def has_module_perms(self , app_label):
        return True  
   
    def save(self , *args , **kwargs):
        return super().save(*args , **kwargs)



    
class Doctor(models.Model):
    user = models.OneToOneField(UserAccount, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    national_id = models.ImageField(null=True, blank=True, default='national.jpg')
    field_title = models.CharField(max_length=150, null=True, blank=True)
    short_intro = models.CharField(max_length=250, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default-doctor.png')
    biography = models.TextField(null=True, blank=True)
    working_place = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)
    cv = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)       
       
    def __str__(self):
        return str(self.username)
    
    
    
    
class Caregiver(models.Model):
    user = models.OneToOneField(UserAccount, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    national_id = models.ImageField(null=True, blank=True, default='national.jpg')
    relation_ship = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)  
    
    def __str__(self):
        return str(self.username)





class Patient(models.Model):
    user = models.OneToOneField(UserAccount, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    national_id = models.ImageField(null=True, blank=True, default='national.jpg')
    age = models.PositiveIntegerField(null=True, blank=True)
    outPatient = models.BooleanField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.SET_NULL)
    diseases = models.ManyToManyField('Disease')
    caregiver = models.ForeignKey(Caregiver, null=True, blank=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, default='default-patient.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.username)  
    
    

    
class PatientStatus(models.Model):
    bodyTemperate = models.FloatField(max_length=100, null=True, blank=True, default=0)
    heartRate = models.FloatField(max_length=100, null=True, blank=True, default=0)
    bloodPressure = models.FloatField(max_length=100, null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 
    
    
    
class Disease(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cause = models.TextField(null=True, blank=True)
    symptom = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 
    
    def __str__(self):
        return str(self.title)
    

class Recommedation(models.Model):
    owner = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    datail = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 
    
    def __str__(self):
        return str(self.title)
    
    
