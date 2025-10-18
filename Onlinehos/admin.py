# from django.contrib import admin
# from django.urls import path, include
# from .models import DoctorReg, PatientReg
# # Register your models here.

# admin.site.register(DoctorReg)
# admin.site.register(PatientReg)

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(DoctorReg)

