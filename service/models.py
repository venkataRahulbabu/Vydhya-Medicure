from django.db import models

class login1(models.Model):
    selectoption=models.CharField(max_length=10)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    
class profilepatient(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=5,null = True)
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phone=models.CharField(max_length=50,null = True)
    dateofbirth=models.CharField(max_length=30,null = True)
    address=models.CharField(max_length=1000,null = True)
    
class doctor(models.Model):
    D_fname=models.CharField(max_length=50)
    D_lname=models.CharField(max_length=50)
    D_email=models.CharField(max_length=50)
    D_phone=models.CharField(max_length=50)
    D_bloodgroup=models.CharField(max_length=50)
    D_dateofbirth=models.CharField(max_length=30)
    D_address=models.CharField(max_length=300)
    D_university=models.CharField(max_length=300)
    D_degree=models.CharField(max_length=300)
    D_license=models.CharField(max_length=50)
    D_awards=models.CharField(max_length=100)
    D_research=models.CharField(max_length=1000)
    D_researchlink=models.CharField(max_length=50,null = True)
    D_previousexperience=models.CharField(max_length=900)
    D_specilization=models.CharField(max_length=100)
    D_fblink=models.CharField(max_length=50,null = True)
    D_instalink=models.CharField(max_length=50,null = True)
    D_twitter=models.CharField(max_length=50,null = True)
    D_others=models.CharField(max_length=1000,null = True)
    D_image=models.ImageField(upload_to='image', blank=True, null=True)
    
    D_hospitalemail=models.CharField(max_length=50)
    
      
class hospital(models.Model):  
    H_name=models.CharField(max_length=50)
    H_branch=models.CharField(max_length=10)
    H_year=models.CharField(max_length=10)
    H_address=models.CharField(max_length=300)
    H_pin=models.CharField(max_length=10)
    H_email=models.CharField(max_length=50)
    H_phone=models.CharField(max_length=20)
    H_photo=models.ImageField(upload_to='image', blank=True, null=True)
    
    H_operation=models.CharField(max_length=5) 
    H_no_n_rooms=models.CharField(max_length=50 , null = True) 
    H_no_s_rooms=models.CharField(max_length=50 , null = True)
    H_ventilators=models.CharField(max_length=50 , null = True)
    H_ecgmonitors=models.CharField(max_length=50 , null = True)
    H_incubators=models.CharField(max_length=50 , null = True)
    H_no_beds=models.CharField(max_length=500 , null = True)
    H_operation_image=models.ImageField(upload_to='image', blank=True, null=True)
    H_operation_oters=models.CharField(max_length=500 , null = True)
    
    
    H_xray=models.CharField(max_length=5) 
    H_xray_image=models.ImageField(upload_to='image', blank=True, null=True)
    H_Xray_oters=models.CharField(max_length=500 , null = True)
    
    H_medicalstore=models.CharField(max_length=5) 
    H_medicalstore_image=models.ImageField(upload_to='image', blank=True, null=True)
    H_medicalstore_oters=models.CharField(max_length=500 , null = True)
    
    H_ctscan=models.CharField(max_length=5) 
    H_ctscan_image=models.ImageField(upload_to='image', blank=True, null=True)
    H_ctscan_oters=models.CharField(max_length=500 , null = True)

    H_bloodtest=models.CharField(max_length=5) 
    H_name_cost=models.CharField(max_length=500 , null = True) 
    H_bloodtest_image=models.ImageField(upload_to='image', blank=True, null=True)
    H_bloodtest_oters=models.CharField(max_length=500 , null = True)
    
    H_emergency=models.CharField(max_length=5) 
    H_ambulance=models.CharField(max_length=50 , null = True) 
    H_no_icu_rooms=models.CharField(max_length=50 , null = True) 
    H_no_beds_icu=models.CharField(max_length=50 , null = True) 
    H_emergency_image=models.ImageField(upload_to='image', blank=True, null=True)
    H_emergency_oters=models.CharField(max_length=500 , null = True)
    
      
class hospital_profile(models.Model): 
    p_H_name=models.CharField(max_length=50)
    p_H_branch=models.CharField(max_length=10)
    p_H_year=models.CharField(max_length=10)
    p_H_address=models.CharField(max_length=300)
    p_H_pin=models.CharField(max_length=10)
    p_H_email=models.CharField(max_length=50)
    p_H_phone=models.CharField(max_length=20)
    P_H_password=models.CharField(max_length=50)
    #p_H_photo=models.ImageField(upload_to='image', blank=True, null=True)
    

class shedule(models.Model):
    time=models.CharField(max_length=20, null = True)
    
    do_sun_timein1=models.CharField(max_length=20, null = True)
    do_sun_timeout1=models.CharField(max_length=20, null = True)
    do_sun_timein2=models.CharField(max_length=20, null = True)
    do_sun_timeout2=models.CharField(max_length=20, null = True)
    do_sun_timein3=models.CharField(max_length=20, null = True)
    do_sun_timeout3=models.CharField(max_length=20, null = True)
    
    do_mon_timein1=models.CharField(max_length=20, null = True)
    do_mon_timeout1=models.CharField(max_length=20, null = True)
    do_mon_timein2=models.CharField(max_length=20, null = True)
    do_mon_timeout2=models.CharField(max_length=20, null = True)
    do_mon_timein3=models.CharField(max_length=20, null = True)
    do_mon_timeout3=models.CharField(max_length=20, null = True)
    
    do_tue_timein1=models.CharField(max_length=20, null = True)
    do_tue_timeout1=models.CharField(max_length=20, null = True)
    do_tue_timein2=models.CharField(max_length=20, null = True)
    do_tue_timeout2=models.CharField(max_length=20, null = True)
    do_tue_timein3=models.CharField(max_length=20, null = True)
    do_tue_timeout3=models.CharField(max_length=20, null = True)
    
    do_wed_timein1=models.CharField(max_length=20, null = True)
    do_wed_timeout1=models.CharField(max_length=20, null = True)
    do_wed_timein2=models.CharField(max_length=20, null = True)
    do_wed_timeout2=models.CharField(max_length=20, null = True)
    do_wed_timein3=models.CharField(max_length=20, null = True)
    do_wed_timeout3=models.CharField(max_length=20, null = True)
    
    do_thu_timein1=models.CharField(max_length=20, null = True)
    do_thu_timeout1=models.CharField(max_length=20, null = True)
    do_thu_timein2=models.CharField(max_length=20, null = True)
    do_thu_timeout2=models.CharField(max_length=20, null = True)
    do_thu_timein3=models.CharField(max_length=20, null = True)
    do_thu_timeout3=models.CharField(max_length=20, null = True)
    
    do_fri_timein1=models.CharField(max_length=20, null = True)
    do_fri_timeout1=models.CharField(max_length=20, null = True)
    do_fri_timein2=models.CharField(max_length=20, null = True)
    do_fri_timeout2=models.CharField(max_length=20, null = True)
    do_fri_timein3=models.CharField(max_length=20, null = True)
    do_fri_timeout3=models.CharField(max_length=20, null = True)
    
    do_sat_timein1=models.CharField(max_length=20, null = True)
    do_sat_timeout1=models.CharField(max_length=20, null = True)
    do_sat_timein2=models.CharField(max_length=20, null = True)
    do_sat_timeout2=models.CharField(max_length=20, null = True)
    do_sat_timein3=models.CharField(max_length=20, null = True)
    do_sat_timeout3=models.CharField(max_length=20, null = True)
    
    hos_email=models.CharField(max_length=50)
    doc_email=models.CharField(max_length=50)
    
class appointment(models.Model):
    Doctor_email=models.CharField(max_length=50)
    p_email=models.CharField(max_length=50)
    Hosp_email=models.CharField(max_length=50)
    timein=models.CharField(max_length=10)
    timeout=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    #day=models.CharField(max_length=50)
    p_fname=models.CharField(max_length=50)
    p_lame=models.CharField(max_length=50)
    p_phone=models.CharField(max_length=50)
    p_gender=models.CharField(max_length=10)
    p_date_of_birth=models.CharField(max_length=10)
    p_address=models.CharField(max_length=500)
    p_hospital_name=models.CharField(max_length=500)
    p_doctor=models.CharField(max_length=50)
    reason=models.CharField(max_length=500, null = True)
    