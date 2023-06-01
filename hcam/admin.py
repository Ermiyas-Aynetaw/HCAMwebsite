from django.contrib import admin

# Register your models here.
from hcam.models import Hospital, Service

admin.site.register(Hospital)
admin.site.register(Service)