from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Patient

def patient_register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']

        user = User.objects.create_user(username=username, password=password)
        Patient.objects.create(user=user, age=age, gender=gender, phone=phone)
        return redirect("login")
    return render(request, "patient_register.html")

def doctor_dashboard(request):
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, "doctor_dashboard.html", {"appointments": appointments})

def admin_dashboard(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    appointments = Appointment.objects.all()
    return render(request, "admin_dashboard.html", {
        "patients": patients,
        "doctors": doctors,
        "appointments": appointments
    })
