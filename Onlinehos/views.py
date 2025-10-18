from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.models import User,auth

# Create your views here.
def main(request):
    return render(request,'main.html')

def dr_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']   
        if DoctorReg.objects.filter(dr_user__username=uname).exists():
            dr=DoctorReg.objects.get(dr_user__username=uname)
            print(dr.is_approved)
            if dr.is_approved=='yes':
                u=auth.authenticate(username=uname,password=password)
                if u is not None:
                    auth.login(request,u)
                    return redirect(dr_welcome)
                else:
                    context ={
                        'key':'invaild user'
                    }
                    return render(request,'dr_login.html',context)
            elif dr.is_approved=='no':
                context ={
                    'key':'user is rejected'
                }
                return render(request,'dr_login.html',context)
            else:
                context={
                    'key':'waiting'
                }
                return render(request,'dr_login.html',context)
        else:
            context ={
                'key':'invaild user'
            }
            return render(request,'dr_login.html',context)

    return render(request,'dr_login.html')


def dr_reg(request):
    if request.method=='POST':
        dname=request.POST['dname']
        Email=request.POST['email']
        ages=request.POST['age']
        uname=request.POST['uname']
        qualification=request.POST['qualification']
        drid=request.POST['drid']
        nowd=request.POST['nowh']
        drsp=request.POST['drsp']
        Password=request.POST['password'] 
        cpassword=request.POST['cpassword']
        phone=request.POST['phone']
        dcer=request.FILES['dcer']
        image=request.FILES['image']
        if Password==cpassword:
            if User.objects.filter(username=uname).exists():
                context = {
                'msg':'User already exists...'
                }
                return render(request,'dr_reg.html',context)
            else:
                User.objects.create_user(username=uname,first_name=dname,email=Email,password=Password).save()
                user=User.objects.get(username=uname)
                DoctorReg(dr_user=user,age=ages,qualification=qualification,drid=drid,phone=phone,nowd=nowd,drsp=drsp,dcer=dcer,image=image).save()
                context = {
                'msg':'Successfully registed'  
                }
                return render(request,'dr_reg.html',context)
        else:
            context = {
            'msg':'Password does not match...'
            }
            return render(request,'dr_reg.html',context)
    return render(request,'dr_reg.html')

def dr_welcome(request):
    drr=DoctorReg.objects.get(dr_user__username=request.user)
    context ={
        'drr':drr
    }
    return render(request,'dr_welcome.html',context)


   
def view_doctor(request):
    doc=DoctorReg.objects.get(dr_user__username=request.user)
    context ={
        'doc':doc
    }
    return redirect('user_view_doctor')

def user_view_doctor(request):
    # your view logic here
    return redirect('user_view_doctor')


def update_doctor(request):
    doc=DoctorReg.objects.get(dr_user__username=request.user)
    context ={
        'doc':doc,
        
    }
    if request.method=='POST':
        doc.dname=request.POST['dname']
        doc.email=request.POST['email']
        doc.age=request.POST['age']
        doc.qualification=request.POST['qualification']
        doc.phone=request.POST['phone']
        
        doc.save()
        return redirect(view_doctor)
    return render(request,'update_doctor.html',context)

        
def log_out(request):
    logout(request)
    return redirect(dr_login)


# patient functions 

def patient_login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        if User.objects.filter(username=uname).exists():
            u=auth.authenticate(username=uname,password=password)
            print(u)
            if u is not None:
                auth.login(request,u) 
                return redirect(patient_welcome)
            else:
                context= {
                    'msg':'invaild user'
                }
                return render(request,'patient_login.html',context)
        else:
            context= {
                 'msg':'invaild user'
            }
            return render(request,'patient_login.html',context)
    return render(request,'patient_login.html')

def patient_reg(request):
    if request.method=='POST':
        name=request.POST['pname']
        pid=request.POST['pid']
        uname=request.POST['uname']
        Password=request.POST['password'] 
        cpassword=request.POST['cpassword']
        age=request.POST['age']
        phone=request.POST['phone']
        blg=request.POST['blg']
        if Password==cpassword:
            if User.objects.filter(username=uname).exists():
                context = {
                'msg':'user already exists...'
                }
                return render(request,'patient_reg.html',context)
            else:
                User.objects.create_user(username=uname,first_name=name,password=Password).save()
                pr=User.objects.get(username=uname)
                PatientReg(user=pr,pid=pid,age=age,phone=phone,blg=blg).save()
                context = {
                'msg':'successfully registed'
                }
                return render(request,'patient_reg.html',context)
        else:
            context = {
            'msg':'password does not match...'
            }
            return render(request,'patient_reg.html',context)
    return render(request,'patient_reg.html')

def patient_welcome(request):
    return render(request,'patient_welcome.html')
  
def view_patient_profile(request):
    return render(request,'view_patient_profile.html')

  
def patient_update(request):  
    pat=PatientReg.objects.get(user__username=request.user)
    context ={
        'pat':pat,
    }
    if request.method=='POST':
        pat.pname=request.POST['pname']
        pat.age=request.POST['age']
        pat.phone=request.POST['phone']
        pat.save()
        return redirect(patient_welcome)
    return render(request,'patient_update.html',context)

   
def view_patient(request):
    pat=PatientReg.objects.get(user__username=request.user)
    context ={
        'pat':pat
    }
    return render(request,'view_patient.html',context)
    
def log_outt(request):
    logout(request) 
    return redirect(patient_login)

def user_view_doctor(request):
    if request.method == 'POST':
        view=request.POST['field']
        us=DoctorReg.objects.filter(drsp=view)
        context ={
            'us':us
        }
        return render(request,'user_view_doctor.html', context)
    return render(request,'user_view_doctor.html')

def dr_view_choose_doctor(request,id):
    us=DoctorReg.objects.get(id=id)
    aa=PatientReg.objects.get(user__username=request.user)     # get value of now login Patient
    context = {
        'key':us
    } 
    if request.method == 'POST':
        var=request.POST['date']
        Appointment(patient = aa ,doctor =us,date=var).save()
        return redirect(take_appointment)
    return render(request,'dr_view_choose_doctor.html',context)

    
def take_appointment(request):
    return render(request,'take_appointment.html')
  
def dr_view_appo_for_patient(request):
    aa=DoctorReg.objects.get(dr_user__username=request.user)   # get value of now login doctor
    bb=Appointment.objects.filter(doctor = aa , approve = 'Waiting')
    context ={
        'app':bb
    }
    return render(request,'dr_view_appo_for_patient.html',context)
   

def dr_view_one_appo_patient(request,pk):
    cc = Appointment.objects.get(id = pk)
    context = {
        'dd':cc
    }
    if request.method == 'POST':
        ee = request.POST['options']
        if ee == 'Waiting':
            return redirect(dr_view_appo_for_patient)
        elif ee == 'Accept':
            Appointment.objects.filter(id = pk).update(approve = 'Accept')
            return redirect(accepted_appointment)
        elif ee == 'Reject':
            Appointment.objects.filter(id = pk).update(approve = 'Reject')
            return redirect(rejected_appointment)
    return render(request,'dr_view_one_appo_patient.html',context)
    

   
def accepted_appointment(request):
    aa=DoctorReg.objects.get(dr_user__username=request.user)   # get value of now login doctor
    bb=Appointment.objects.filter(doctor = aa , approve = 'Accept')
    context ={
        'app':bb
    }
    return render(request,'accepted_appointment.html',context)

def rejected_appointment(request):
    aa=DoctorReg.objects.get(dr_user__username=request.user)   # get value of now login doctor
    bb=Appointment.objects.filter(doctor = aa , approve = 'Reject')
    context ={
        'app':bb
    }
    return render(request,'rejected_appointment.html',context)


def appointment_history(request):
    aa=PatientReg.objects.get(user__username=request.user)   # get value of now login doctor
    print(request.user)
    print(aa.id)
    bb=Appointment.objects.filter(patient = aa)
    context ={
        'app':bb
    }
    return render(request, 'appointment_history.html', context)

