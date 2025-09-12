from django.urls import path
from . import views

urlpatterns = [
    path("patient/register/", views.patient_register, name="patient_register"),
    path("doctor/dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("admin/dashboard/", views.admin_dashboard, name="admin_dashboard"),
]
