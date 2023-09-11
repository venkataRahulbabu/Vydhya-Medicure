from django.contrib import admin
from service.models import login1
from service.models import profilepatient
from service.models import doctor
from service.models import hospital
from service.models import hospital_profile
from service.models import shedule


class login_log(admin.ModelAdmin):
    list_display=('selectoption','fname','lname','email','password','gender')
    
class patient_profile(admin.ModelAdmin):
    list_display=('fname','lname','bloodgroup','email','gender','phone','dateofbirth','address')
    
class doc_tor(admin.ModelAdmin):
    list_display=('D_fname','D_lname','D_email','D_phone','D_bloodgroup','D_dateofbirth','D_address','D_university','D_degree','D_license','D_awards','D_research','D_reasearchlink','D_previousexperience','D_specilization','D_fblink','D_instalink','D_twitter','D_others','D_image')
    
class hos_pital(admin.ModelAdmin):
    list_display=('H_name','H_branch','H_year','H_address','H_pin','H_email','H_phone','H_photo','H_operation','H_no_n_rooms','H_no_s_rooms','H_ventilators','H_ecgmonitors','H_incubators','H_no_beds','H_operation_image','H_operation_oters','H_xray','H_xray_image','H_Xray_oters','H_medicalstore','H_medicalstore_image','H_medicalstore_oters','H_ctscan','H_ctscan_image','H_ctscan_oters','H_bloodtest','H_name_cost','H_bloodtest_image','H_bloodtest_oters','H_emergency','H_ambulance','H_no_icu_rooms','H_no_beds_icu','H_emergency_image','H_emergency_oters')
    
class hospital_p_rofile(admin.ModelAdmin):
    list_display=('p_H_name','p_H_branch','p_H_year','p_H_address','p_H_pin','p_H_email','p_H_phone','p_H_photo')
    
class she_dule(admin.ModelAdmin):
    list_display=('time','do_sun_timein1','do_sun_timeout1','do_sun_timein2','do_sun_timeout2','do_sun_timein3','do_sun_timeout3','do_mon_timein1','do_mon_timeout1','do_mon_timein2','do_mon_timeout2','do_mon_timein3','do_mon_timeout3','do_tue_timein1','do_tue_timeout1','do_tue_timein2','do_tue_timeout2','do_tue_timein3','do_tue_timeout3','do_wed_timein1','do_wed_timeout1','do_wed_timein2','do_wed_timeout2','do_wed_timein3','do_wed_timeout3','do_thu_timein1','do_thu_timeout1','do_thu_timein2','do_thu_timeout2','do_thu_timein3','do_thu_timeout3','do_fri_timein1','do_fri_timeout1','do_fri_timein2','do_fri_timeout2','do_fri_timein3','do_fri_timeout3','do_sat_timein1','do_sat_timeout1','do_sat_timein2','do_sat_timeout2','do_sat_timein3','do_sat_timeout3','hos_email','doc_email')   
    

admin.site.register(login1,login_log)
admin.site.register(profilepatient,patient_profile)
# admin.site.register(doctor,doc_tor)
# admin.site.register(hospital,hos_pital)
# admin.site.register(hospital_profile,hospital_p_rofile)
# admin.site.register(shedule,she_dule)
# Register your models here.
