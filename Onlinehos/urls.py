from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),

    # Doctor URLs
    path('dr_login/', views.dr_login, name='dr_login'),
    path('dr_login/dr_reg/', views.dr_reg, name='dr_reg'),
    path('dr_welcome/', views.dr_welcome, name='dr_welcome'),
    path('update_doctor/', views.update_doctor, name='update_doctor'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('dr_view_appo_for_patient/', views.dr_view_appo_for_patient, name='dr_view_appo_for_patient'),
    path('dr_view_one_appo_patient/<str:pk>/', views.dr_view_one_appo_patient, name='dr_view_one_appo_patient'),
    path('accepted_appointment/', views.accepted_appointment, name='accepted_appointment'),
    path('rejected_appointment/', views.rejected_appointment, name='rejected_appointment'),
    path('patient_welcome/appointment_history/', views.appointment_history, name='appointment_history'),
    path('dr_view_choose_doctor/<str:id>/', views.dr_view_choose_doctor, name='dr_view_choose_doctor'),

    # Patient URLs
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_login/patient_reg/', views.patient_reg, name='patient_reg'),
    path('patient_welcome/', views.patient_welcome, name='patient_welcome'),
    path('patient_welcome/user_view_doctor/', views.user_view_doctor, name='user_view_doctor'),
    path('patient_welcome/user_view_doctor/patient_welcome/', views.user_view_doctor, name='user_view_doctor_duplicate'),
    path('view_patient_profile/', views.view_patient_profile, name='view_patient_profile'),
    path('patient_update/', views.patient_update, name='patient_update'),
    path('patient_welcome/view_patient/', views.view_patient, name='view_patient'),
    path('take_appointment/', views.take_appointment, name='take_appointment'),

    # Logout
    path('log_out/', views.log_out, name='log_out'),
]
