"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views
from project import view
from project import viewshosptial


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('_signinn/',views.signinn,name='signinn'),
    path('signup/',views.signup,name='signup'),
    path('saveform1/',views.login,name='login'),
    path('otp/',views.otpsignp,name='otp'),
    path('query/',views.query,name='query'),
    path('forget/',views.forget,name='forget'),
    path('forget_password/',views.forget_email_otp,name='for_pas'),
    path('@otp/',views.forget_p_otp,name='for_otp'),
    
    path('patient/',view.indexpatient,name='indexpatient'),
    path('patientabout/',view.about,name='pabout'),
    path('patientservice/',view.service,name='pservice'),
    path('patientdoctors/',view.doctors,name='pdoctors'),
    path('patientappoinment/',view.appointment1,name='pappointment'),
    path('patientsearch/',view.search,name='psearch'),
    path('patientcontact/',view.contact,name='pcontact'),
    path('patienteditprofile/',view.editprofile,name='peditprofile'),
    path('patienthempandsupport/',view.helpandsupport,name='phelpandsupport'),
    path('patientlogout/',view.logout,name='plogout'),
    path('patientemergencycare/',view.emergencycare,name='pemergencycare'),
    path('patientoperationandsurgery/',view.operationandsurgery,name='poperationandsurgery'),
    path('patientctscan/',view.ctscan,name='pctscan'),
    path('patientothertest/',view.othertest,name='othertest'),
    path('patientmedicineandpharmacy/',view.medicineandpharmacy,name='medicineandpharmacy'),
    #path('patientbloodtest/',viewspatient.bloodtest,name='bloodtest'),
    path('patientedit/',view.pedit,name='pedit'),
    
    path('otp1/', viewshosptial.aotp, name='aotp'),
    path('hsiginup/',viewshosptial.hospitalsignup,name='hospitalsignup'),
    #path('hdashboard/',viewshosptial.hdashboard,name='hdashboard'),
    path('allpatient/',viewshosptial.allpatient,name='allpatient'),
    #path('addpatient/',viewshosptial.addpatient,name='addpatient'),
    path('adddoctor/',viewshosptial.adddoctor,name='adddoctor'),
    path('addoctor/',viewshosptial.addoctor,name='addoctor'),
    path('alldoctor/',viewshosptial.alldoctor,name='alldoctor'),
    path('bookappointment/',viewshosptial.bookappointment_hospital,name='bookappointment_hospital'),
    #path('logout/',viewshosptial.logout,name='logout'),
    #path('editprofile/',viewshosptial.editprofile,name='editprofile'),
    
    
    path('hospitalsgup/',viewshosptial.hospitalsgup,name='hospitalsgup'),
    path('bookappointment/',viewshosptial.bookappointment,name='bookappointment'),
    path('edithospital/',viewshosptial.edithospital, name='edithospital'),
    path('edit/',viewshosptial.edit, name='edit'),
    
    path('hosp_index/',viewshosptial.hosp_index, name='hosp_index'),
    path('logoutt/',viewshosptial.logoutt, name='logoutt'),
    path('profile/',viewshosptial.profile, name='profile'),
    path('app/',viewshosptial.app, name='app'),
    
    
    path('appoint/',view.appoint, name='appoint'),
    path('appoint2/',view.appoint2, name='appoint2'),
    path('appoint3/',view.appoint3, name='appoint3'),
    path('appoint4/',view.appoint4, name='appoint4'),
    
    path('apoi/',view.apoi, name='apoi'),
    path('bookappointment__hospital/',view.bookappointment__hospital, name='bookappointment__hospital'),

    
    
    
    
    
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
