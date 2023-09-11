from django.http import HttpResponse
from django.shortcuts import render
from service.models import login1
from django.db import connection
from service.models import profilepatient
from service.models import doctor
from service.models import hospital
from service.models import hospital_profile
from service.models import shedule
from service.models import appointment
import random
from django.core.mail import send_mail
from datetime import date
from django.core.mail import send_mail
from datetime import datetime


from PIL import Image



def hosp_index(request):
    return render(request,"hospitalindex.html")

def hospitalsgup(request):
    return render(request,"signuphospital.html")
    

def hospitalsignup(request):
    if request.method=="POST":
         p_H_name=request.POST.get('hname')
         p_H_branch=request.POST.get('branch')
         p_H_year=request.POST.get('estyear')
         p_H_address=request.POST.get('address')
         p_H_pin=request.POST.get('pin')
         p_H_email=request.POST.get('email')
         p_H_phone=request.POST.get('phone')
         P_H_password=request.POST.get('password')
        #  p_H_photo=request.FILES['myfile']
        #  photo=json.dumps(p_H_photo)
         emil =  hospital_profile.objects.raw("select id,p_H_email from service_hospital_profile")
         j=0
         if len(emil)!=0: 
              for i in emil:
                 if i.p_H_email==p_H_email:
                     j=j+1 
         
              if j!=0 :
                  n="emilid already exist"
                  return render(request,"home.html",{'n':n})   
         if j==0:                        
              request.session['p_H_name']=[p_H_name]
              request.session['p_H_branch']=[p_H_branch]
              request.session['p_H_year']=[p_H_year]
              request.session['p_H_address']=[p_H_address]
              request.session['p_H_pin']=[p_H_pin]
              request.session['p_H_email']=[p_H_email]
              request.session['p_H_phone']=[p_H_phone]
            #   request.session['p_H_photo']=[p_H_photo]
              request.session['P_H_password']=[P_H_password]
            #   Serialized_object = JSON.stringify(Object)
            #   otp(request)
              email=request.session['p_H_email']
              OTP = random.randint(11111,99999)
              send_mail(
              'OTP',
              "your login otp is " +str(OTP),
              'vydya.doctor@gmail.com',
              email,
              )
              request.session['otp']=[OTP] 
              OTP=request.session['otp']     
              print(OTP[0]) 
    return render(request,"otpform.html")
         
         
         
         
         
# def otp(request):
#     m=""
#     if 'p_H_email' in request.session:
#         email=request.session['p_H_email']
#         print(email)
#         OTP = random.randint(11111,99999)
#         send_mail(
#         'OTP',
#         "your login otp is " +str(OTP),
#         'vydya.doctor@gmail.com',
#         email,
#         )
#         request.session['otp']=[OTP]       
#     else:
#         m='please enter the details first'
#         return render(request,"home.html",{'m':m})
    
        
def aotp(request):
    print("hi\n\n\n\n\n\n\n")
    if 'otp' in request.session:
        OTP=request.session['otp']
        
        print(OTP) 
        if request.method=="POST": 
            print("hiiii\n\n\n")
            otp=request.POST.get('o')
        
        print(otp)
        
        if otp==str(OTP[0]):
            p_H_name=request.session['p_H_name']
            p_H_branch=request.session['p_H_branch']
            p_H_year=request.session['p_H_year']
            p_H_address=request.session['p_H_address']
            p_H_pin=request.session['p_H_pin']
            p_H_email=request.session['p_H_email']
            p_H_phone=request.session['p_H_phone']
            #p_H_photo=request.session['p_H_photo']
            P_H_password=request.session['P_H_password']
            hos=hospital_profile(p_H_name=p_H_name[0], p_H_branch=p_H_branch[0], p_H_year=p_H_year[0], p_H_address=p_H_address[0], p_H_pin=p_H_pin[0], p_H_email=p_H_email[0] ,p_H_phone=p_H_phone[0], P_H_password=P_H_password[0])
            hosp=hospital(H_name=p_H_name[0],H_branch=p_H_branch[0],H_year=p_H_year[0],H_address=p_H_address[0],H_pin=p_H_pin[0],H_email=p_H_email[0] , H_phone=p_H_phone[0] )
            app=appointment( Doctor_email="None",p_email="None",Hosp_email="None",timein="None",timeout="None",date="None",p_fname="None",p_lame="None",p_phone="None",p_gender="None",p_date_of_birth="None",p_address="None",p_hospital_name="None",p_doctor="None",reason="None")
            hos.save()
            hosp.save()
            app.save()
            del request.session['p_H_name']
            del request.session['p_H_branch']
            del request.session['p_H_year']
            del request.session['p_H_address']
            del request.session['p_H_pin']
            del request.session['p_H_email']
            del request.session['p_H_phone']
            del request.session['P_H_password']
            m='login success'
            del request.session['otp']
            return render(request,"home.html",{'m':m})
            
        else:
            m='otp is incorrect'
            return render(request,"otpform.html",{'m':m})
    else:
        m='please fill all the details'
        return render(request,"home.html",{'m':m})
           
def edit(request):
    if 'ss' in request.session:
        return render(request,"hospitaledit.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
            

def edithospital(request):
    if 'ss' in request.session:
        email=request.session['ss']
        if request.method=="POST":
            H_name=request.POST.get('H_name')
            H_branch=request.POST.get('H_branch')
            H_year=request.POST.get('H_year')
            H_address=request.POST.get('H_address')
            H_pin=request.POST.get('H_pin')
            H_email=request.POST.get('H_email')
            H_phone=request.POST.get('H_phone')
            H_no_n_rooms=request.POST.get('H_no_n_rooms')
            H_no_s_rooms=request.POST.get('H_no_s_rooms')
            H_photo=request.POST.get('H_photo')
            
        print( H_no_n_rooms)
        print(email)
        
        
        print(H_name)
        print( H_branch)
        print(H_year)
        print(H_address)
        print(H_pin)
        print(H_email)
        print(H_phone)
        print(H_no_n_rooms)
        print(H_no_s_rooms)
        
        cursor=connection.cursor()
        #hospe=hospital(H_name=H_name, H_branch=H_branch, H_year=H_year, H_address=H_address, H_pin=H_pin, H_email=H_email ,H_phone=H_phone, H_photo=H_photo ,H_no_n_rooms=H_no_n_rooms,H_no_s_rooms=H_no_s_rooms )
        cursor.execute("update service_hospital set H_name=%s,H_branch=%s,H_year=%s,H_address=%s,H_pin=%s,H_email=%s,H_phone=%s,H_photo=%s,H_no_n_rooms=%s,H_no_s_rooms=%s where H_email = %s ",[H_name, H_branch, H_year, H_address, H_pin, H_email ,H_phone, H_photo,H_no_n_rooms,H_no_s_rooms,H_email])
        # hospe.save()
        return render(request,"hospitalindex.html")
            
            
        
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
        
               
            
    


def allpatient(request):
    m=""
    if 'ss' in request.session:
       today = date.today()
       emailid = request.session['ss']
       a=appointment.objects.raw("select * from service_appointment where Hosp_email = %s ",[emailid])
       print(a[0].p_fname)
       return render(request,"hospital_allpat.html",{'a':a})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
    

    
    

def alldoctor(request):
   
    if 'ss' in request.session:
       email=request.session['ss']
       a=doctor.objects.raw("select * from service_doctor where D_hospitalemail= %s",[email])
       print(a)
       print(a[0])
       print(a[0].D_fname)
       return render(request,"hospital_allDoctors.html",{'a':a})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
def addoctor(request):
    if 'ss' in request.session:
       email=request.session['ss']
       #a=doctor.objects.raw("select * from service_doctor where D_hospitalemail=%s  ",[email])
       return render(request,"hospital_addDoctors.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
    
def adddoctor(request):
    m=""
    if 'ss' in request.session:
        emailid = request.session['ss']
        if request.method=="POST":
            D_fname=request.POST.get('fname')
            D_lname=request.POST.get('lname')
            D_phone=request.POST.get('phone')
            D_email=request.POST.get('email')
            D_bloodgroup=request.POST.get('bloodgroup')
            D_dateofbirth=request.POST.get('dob')
            D_address=request.POST.get('address')
            D_university=request.POST.get('university')
            D_degree=request.POST.get('degreeheld')
            D_license=request.POST.get('license')
            D_awards=request.POST.get('honsawards')
            D_specilization=request.POST.get('specialization')
            D_previousexperience=request.POST.get('prevexp')
            D_research=request.POST.get('research')
            D_others=request.POST.get('internship')
            D_researchlink=request.POST.get('researchlink')
            D_twitter=request.POST.get('twitter')
            D_fblink=request.POST.get('fb')
            D_instalink=request.POST.get('insta')
            D_image=request.FILES['image']
            
        doc=doctor(D_fname=D_fname, D_lname=D_lname, D_phone=D_phone, D_email=D_email, D_bloodgroup=D_bloodgroup, D_dateofbirth=D_dateofbirth, D_address=D_address, D_university=D_university, D_degree=D_degree, D_license=D_license ,D_awards=D_awards ,D_specilization=D_specilization ,D_previousexperience=D_previousexperience, D_research=D_research,  D_others=D_others ,D_researchlink=D_researchlink, D_twitter=D_twitter ,D_fblink=D_fblink ,D_instalink=D_instalink ,D_image=D_image, D_hospitalemail=emailid)
        doc.save()
        # print(D_fname)
        # print(D_lname)
        # print(D_phone)
        # print(D_email)
        # print(D_bloodgroup)
        # print(D_dateofbirth)
        # print(D_address)
        # print(D_license)
        # print(D_awards)
        # print(D_specilization)
        # print(D_previousexperience)
        # print(D_research)
        # print(D_others)
        # print(D_researchlink)
        # print(D_twitter)
        # print(D_fblink)
        # print(D_instalink)
        
        n="doctor added successfully"
        return render(request,"hospitalindex.html",{'n':n}) 
    
    else:
        n="session expired"
        return render(request,"home.html",{'n':n})  
    
    
def app(request):
    if 'ss' in request.session:
        print("hi")
        if request.method=="POST":
            H=request.POST.get('i1')
            D=request.POST.get('i2')
            request.session['a']=D
            return render(request,"hospital_appoint.html")
    
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
            
        
    
    

    
    
def bookappointment_hospital(request):
    if 'ss' in request.session:
        count=0
        if 'a' in request.session:
            Hosp_email=request.session['ss']
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
                b=hospital_profile.objects.raw("select * from service_hospital_profile where p_H_email=%s",[Hosp_email])
                p_hospital_name=b[0].p_H_name
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
                "name :" +p_fname+" "+p_lame+"\n"+"appointment timings "+timein +" to "+timeout +"\n"+"date: "+date+"\n"+"doctor name:"+p_doctor,
                'vydya.doctor@gmail.com',
                [p_email],
        
                )
                
                
                

                  
                  
                return render(request,"hospitalindex.html",{'n':m}) 
                    
            
                    
            
            
            
            
            
    #    a=doctor.objects.raw("select * from service_doctor where D_hospitalemail= and date = %s ",[email])
       
              
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    

def bookappointment(request):  
    if 'ss' in request.session:
       email=request.session['ss']
       p=request.session['doc']
       if request.method=="POST":
            #  p_fname=request.POST.get('i')
            #  p_lame=request.POST.get('i')
            #  p_phone=request.POST.get('i')
            #  p_gender=request.POST.get('i')
            #  p_date_of_birth=request.POST.get('i')
            #  p_address=request.POST.get('i')
            #  p_email=request.POST.get('i')
            #  date=request.POST.get('i')
             
             
             
             
             
             
             
        request.session['doc']=p
    #    a=doctor.objects.raw("select * from service_doctor where D_hospitalemail= and date = %s ",[email])
       
       return render(request,"hospital_appontment.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
    
def logoutt(request):
    m=""
    if 'ss' in request.session:
        del request.session['ss']
        return render(request,"home.html")
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
      
    
def profile(request):  
    m=""
    if 'ss' in request.session:
        if request.method=="POST":
            H=request.POST.get('i1')
            D=request.POST.get('i2') 
            emailid = request.session['ss']
            print(emailid)
            print(H)
            print(D)
            print()
            print()
            a=doctor.objects.raw("select * from service_doctor where D_email = %s ",[D])
            # D_hospitalemail = %s and
           # a=doctor.objects.raw("select * from service_doctor")
            print(a)
            print(a[0])
            print(a[0].D_fname)
            print(a[0].D_hospitalemail)
            print(a[0].D_email)
            print()
            print()
            return render(request,"profile.html",{'a':a[0]})
    else:
        m="your session has expired please login again"
        return render(request,"home.html",{'m':m})
    
    
# def logout(request):
    
# def editprofile(request):


 
            
            
            
        
    
    


    






