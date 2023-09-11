from django.http import HttpResponse
from django.shortcuts import render
from service.models import login1
from django.core.mail import send_mail
from django.db import connection
from service.models import profilepatient
from service.models import doctor
from service.models import hospital_profile
from service.models import hospital
from service.models import shedule
from service.models import appointment
import random

from datetime import date

from datetime import datetime

    
def pedit(request):
    m=""
    if 'ss' in request.session:     
         emailid = request.session['ss']
         if request.method=="POST":
             fname=request.POST.get('fname')
             lname=request.POST.get('lname')
             bloodgroup=request.POST.get('bloodgroup')
            #  emailid=request.POST.get('email')
             gender=request.POST.get('Gender')
             phone=request.POST.get('phone')
             dateofbirth=request.POST.get('dateofbirth')
             address=request.POST.get('address')
             cursor=connection.cursor()
             cursor.execute("update service_profilepatient set fname=%s,lname=%s,bloodgroup=%s,gender=%s,phone=%s,dateofbirth=%s,address=%s where email = %s ",[fname,lname,bloodgroup,gender,phone,dateofbirth,address,emailid])
             m="edit is success"    
         return render(request,"indexpatient.html",{'m':m})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
        
        
def apoi(request):
    m=""
    if 'ss' in request.session:
        if request.method=="POST":
            H=request.POST.get('i1')
            D=request.POST.get('i2')
            request.session['a']=D
            return render(request,"hospital__appoint.html") 
        
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
    
def bookappointment__hospital(request):
    if 'ss' in request.session:
        count=0
        if 'a' in request.session:
            
            if request.method=="POST":
                p_email=request.POST.get('email')
                date=request.POST.get('checkin')
                p_fname=request.POST.get('fname')
                p_lame=request.POST.get('lname')
                p_phone=request.POST.get('cnumber')
                p_gender=request.POST.get('Gender')
                p_date_of_birth=request.POST.get('DOB')
                p_address=request.POST.get('address')
                reason=request.POST.get('reason')
                print(p_email)
                print(date)
                print(p_fname)
                print(p_lame)
                print(p_phone)
                print(p_gender)
                print(p_date_of_birth)
                print(p_address)
                print(reason)
                Doctor_email=request.session['a']
                a=doctor.objects.raw("select * from service_doctor where D_email=%s",[Doctor_email])

                fname=a[0].D_fname
                lname=a[0].D_lname
                p_doctor=fname+" "+lname
                Hosp_email=a[0].D_hospitalemail
                print(Hosp_email)
               
                b=hospital_profile.objects.raw("select * from service_hospital_profile where p_H_email=%s",[Hosp_email])
                p_hospital_name=b[0].p_H_name
                today=date
                b=appointment.objects.raw("select * from service_appointment where date=%s",[today])
                for i in b:
                    if i.Doctor_email==Doctor_email:
                        count=count+1
                    
                a=count
                print(count)
                
                if a==0:
                    timein ="9:00AM"
                    timeout="9:10AM"
                if a==1:
                    timein ="9:10AM"
                    timeout="9:20AM"
                if a==2:
                    timein ="9:20AM"
                    timeout="9:30AM"
                if a==3:
                    timein ="9:30AM"
                    timeout="9:40AM"
                if a==4:
                    timein ="9:40AM"
                    timeout="9:50AM"
                if a==5:
                    timein ="9:50AM"
                    timeout="10:00AM"
                if a==6:
                    timein ="10:00AM"
                    timeout="10:10AM"
                if a==7:
                    timein ="10:10AM"
                    timeout="10:20AM"
                if a==8:
                    timein ="10:20AM"
                    timeout="10:30AM"
                if a==9:
                    timein ="10:30AM"
                    timeout="10:40AM"
                if a==10:
                    timein ="10:40AM"
                    timeout="10:50AM"
                if a==11:
                    timein ="10:50AM"
                    timeout="11:00AM"
                if a==12:
                    timein ="11:00AM"
                    timeout="11:10AM"
                if a==13:
                    timein ="11:10AM"
                    timeout="11:20AM"
                if a==14:
                    timein ="11:20AM"
                    timeout="11:30AM"
                if a==15:
                    timein ="11:30AM"
                    timeout="11:40AM"
                if a==16:
                    timein ="11:40AM"
                    timeout="11:50AM"
                if a==17:
                    timein ="11:50AM"
                    timeout="12:00AM"
                # if a>=19:
	            #     m="All slots are booked"
                #     return render(request,"hospital_appontment",{'n':m})
                print(timein)
                m="appointment success"
                app=appointment(Doctor_email=Doctor_email,p_email=p_email,Hosp_email=Hosp_email,timein=timein,timeout=timeout,date=date,p_fname=p_fname,p_lame=p_lame,p_phone=p_phone,p_gender=p_gender,p_date_of_birth=p_date_of_birth,p_address=p_address,p_hospital_name=p_hospital_name,p_doctor=p_doctor,reason=reason)
                app.save()
                send_mail(
                'APPOINTMENT DETAILS',
                "name :" +p_fname+" "+p_lame+"\n"+"appointment timings "+timein +" to "+timeout +"\n"+"date: "+"date"+"\n"+"doctor name:"+p_doctor,
                'vydya.doctor@gmail.com',
                [p_email],
        
                )
   
                return render(request,"indexpatient.html",{'n':m}) 
 
    #    a=doctor.objects.raw("select * from service_doctor where D_hospitalemail= and date = %s ",[email])
       
              
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
               
def indexpatient(request):
    m=""
    if 'ss' in request.session:
       return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def about(request):
    m=""
    if 'ss' in request.session:
       return render(request,"pabout.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    

def service(request):
    m=""
    if 'ss' in request.session:
       return render(request,"pservice.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def doctors(request):
    m=""
    if 'ss' in request.session:
        a=doctor.objects.raw("select * from service_doctor") 
        return render(request,"pteam.html",{'a':a})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def appointment1(request):
    m=""
    if 'ss' in request.session:
       return render(request,"pappointment.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
def appoint(request):
    m=""
    if 'ss' in request.session:
       if request.method=="POST":
                print("hi")
                print()
                print()
                p_email=request.POST.get('email')
                # date=request.POST.get('checkin')
                p_fname=request.POST.get('fname')
                p_lame=request.POST.get('lname')
                p_phone=request.POST.get('cnumber')
                p_gender=request.POST.get('Gender')
                p_date_of_birth=request.POST.get('DOB')
                p_address=request.POST.get('address')
                # reason=request.POST.get('reason')
                
                request.session['p_email']=p_email
                request.session['p_fname']=p_fname
                request.session['p_lame']=p_lame
                request.session['p_phone']=p_phone
                request.session['p_gender']=p_gender
                request.session['p_date_of_birth']=p_date_of_birth
                request.session['p_address']=p_address
                print("hi")
                print()
                print()
                a=hospital_profile.objects.raw("select * from service_hospital_profile")
                return render(request,"pappointment2.html",{'a':a})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    

def appoint2(request):
    m=""
    if 'ss' in request.session:
       if request.method=="POST":
                p_hospital_name=request.POST.get('p_hospital_name')
                b=hospital_profile.objects.raw("select * from service_hospital_profile where p_H_name = %s ",[p_hospital_name])
                D_hospitalemail=b[0].p_H_email
                a=doctor.objects.raw("select * from service_doctor where D_hospitalemail = %s ",[D_hospitalemail])
                request.session['p_hospital_name']=p_hospital_name
                request.session['Hosp_email']=D_hospitalemail
                return render(request,"pappointment3.html",{'a':a})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def appoint3(request):
    m=""
    if 'ss' in request.session:
       if request.method=="POST":
                p_doctor=request.POST.get('p_doctor')
                request.session['p_doctor']=p_doctor
                m="appointment success"
                return render(request,"pappointment4.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
def appoint4(request):
    m=""
    if 'ss' in request.session:
       if request.method=="POST":
                reason=request.POST.get('reason')
                date=request.POST.get('date')
                
                #Doctor_email=request.session['p_doctor']
                p_email=request.session['p_email']
                p_fname=request.session['p_fname']
                p_lame=request.session['p_lame']
                p_phone=request.session['p_phone']
                p_gender=request.session['p_gender']
                p_date_of_birth=request.session['p_date_of_birth']
                p_address=request.session['p_address']
                p_hospital_name=request.session['p_hospital_name']
                p_doctor=request.session['p_doctor']
                Hosp_email=request.session['Hosp_email']
                
                x=p_doctor.split()
                c=doctor.objects.raw("select * from service_doctor where D_hospitalemail=%s ",[Hosp_email])
                for i in c:
                    if i.D_fname==x[0] and i.D_lname==x[1]:
                        Doctor_email=i.D_email
                today=date
                b=appointment.objects.raw("select * from service_appointment where date=%s ",[today])
                for i in b:
                    if i.Doctor_email==Doctor_email:
                        count=count+1
                    
                a=count
                print(count)
                
                if a==0:
                    timein ="9:00AM"
                    timeout="9:10AM"
                if a==1:
                    timein ="9:10AM"
                    timeout="9:20AM"
                if a==2:
                    timein ="9:20AM"
                    timeout="9:30AM"
                if a==3:
                    timein ="9:30AM"
                    timeout="9:40AM"
                if a==4:
                    timein ="9:40AM"
                    timeout="9:50AM"
                if a==5:
                    timein ="9:50AM"
                    timeout="10:00AM"
                if a==6:
                    timein ="10:00AM"
                    timeout="10:10AM"
                if a==7:
                    timein ="10:10AM"
                    timeout="10:20AM"
                if a==8:
                    timein ="10:20AM"
                    timeout="10:30AM"
                if a==9:
                    timein ="10:30AM"
                    timeout="10:40AM"
                if a==10:
                    timein ="10:40AM"
                    timeout="10:50AM"
                if a==11:
                    timein ="10:50AM"
                    timeout="11:00AM"
                if a==12:
                    timein ="11:00AM"
                    timeout="11:10AM"
                if a==13:
                    timein ="11:10AM"
                    timeout="11:20AM"
                if a==14:
                    timein ="11:20AM"
                    timeout="11:30AM"
                if a==15:
                    timein ="11:30AM"
                    timeout="11:40AM"
                if a==16:
                    timein ="11:40AM"
                    timeout="11:50AM"
                if a==17:
                    timein ="11:50AM"
                    timeout="12:00AM"
                # if a>=19:
	            #     m="All slots are booked"
                #     return render(request,"hospital_appontment",{'n':m})
                print(timein)
                m="appointment success"
                app=appointment(Doctor_email=Doctor_email,p_email=p_email,Hosp_email=Hosp_email,timein=timein,timeout=timeout,date=date,p_fname=p_fname,p_lame=p_lame,p_phone=p_phone,p_gender=p_gender,p_date_of_birth=p_date_of_birth,p_address=p_address,p_hospital_name=p_hospital_name,p_doctor=p_doctor,reason=reason)
                app.save()
                send_mail(
                'APPOINTMENT DETAILS',
                "name " +p_fname+" "+p_lame+"\n"+"appointment timings "+timein +" to "+timeout,
                'vydya.doctor@gmail.com',
                [p_email],
                )
                m="appointment success"
                return render(request,"pappointment4.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def search(request):
    m=""
    if 'ss' in request.session:
        return render(request,"psearch.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def contact(request):  
    m=""
    if 'ss' in request.session:
        return render(request,"pcontact.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def editprofile(request):
    m=""
    if 'ss' in request.session:
        emailid = request.session['ss']
        a=profilepatient.objects.raw("select * from service_profilepatient where email = %s ",[emailid])
        return render(request,"pedit.html",{'a':a[0]})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def logout(request):
    m=""
    if 'ss' in request.session:
        del request.session['ss']
        return render(request,"home.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    




def emergencycare(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
 
def operationandsurgery(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
 
def ctscan(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
 
def othertest(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def medicineandpharmacy(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})

def bloodtest(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
 
def helpandsupport(request):
    m=""
    if 'ss' in request.session:
        return render(request,"indexpatient.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})






