from django.contrib import admin

# Register your models here.
from users.models import UserAccount, Doctor, Patient, Caregiver, PatientStatus, Disease, Recommedation

admin.site.register(UserAccount)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Caregiver)
admin.site.register(PatientStatus)
admin.site.register(Disease)
admin.site.register(Recommedation)