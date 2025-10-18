from django.db import models
from django.contrib.auth.models import User

class DoctorReg(models.Model):
    dr_user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    age = models.CharField(max_length=100, null=True)
    qualification = models.CharField(max_length=100, null=True)
    drid = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    nowd = models.IntegerField(null=True)
    dcer = models.FileField(upload_to='upload_img', null=True)
    drsp = models.CharField(max_length=100, null=True)
    is_approved = models.CharField(max_length=100, default='waiting', null=True)

    def __str__(self):
        return self.dr_user.first_name + ' ' + self.is_approved


class PatientReg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pid = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    blg = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.first_name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(DoctorReg, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(PatientReg, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    approve = models.CharField(max_length=50, default='Waiting')

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date}"
