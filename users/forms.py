
from django.forms import ModelForm
from .models import Patient, Caregiver, Doctor, Disease, Recommedation, PatientStatus

from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm



class PatientForm(ModelForm):
    
    class Meta:
        model = Patient
        fields = ['first_name', 'middle_name', 'last_name', 'age','email', 'username', 'location', 
                  'outPatient', 'doctor', 'caregiver', 'diseases', 'national_id', 'profile_image'
                  ]

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class CaregiverForm(ModelForm):
    
    class Meta:
        model = Caregiver
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'username', 
                  'location', 'relation_ship', 'national_id', 'profile_image',
                  ]
        
    def __init__(self, *args, **kwargs):
        super(CaregiverForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
    

class DoctorForm(ModelForm):
    
    class Meta:
        model = Doctor
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'username', 'location', 'field_title', 
                  'short_intro', 'biography', 'working_place', 'cv', 'national_id', 'profile_image'
                  ]    
        
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class DiseaseForm(ModelForm):
    
    class Meta:
        model = Disease
        fields = '__all__'
      
        
class RecommendationForm(ModelForm):
    
    class Meta:
        model = Recommedation
        fields = '__all__'
        
            
        
class PatientStatusForm(ModelForm):    
    class Meta:
        model = PatientStatus
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name', 'email', 'username', 'type', 'password1', 'password2']
        
        labels = {
            'first_name':'Name'
        }
                
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})