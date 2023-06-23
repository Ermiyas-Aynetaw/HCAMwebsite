from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid


# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    more_information = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    service = models.ManyToManyField('Service')
    social_website = models.CharField(max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    hospital_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)   
    
    def __str__(self):
        return str(self.name)
    
 
    
class Service(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    service_image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False) 
    
    def __str__(self):
        return str(self.title)
    
    
    