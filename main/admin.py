from django.contrib import admin
from .models import *
# Register your models here.



admin.site.site_header = 'DTS Insurance Services'                    # default: "Django Administration"
admin.site.index_title = 'Control Panel'                 # default: "Site administration"
admin.site.site_title = 'DTS Admin Pannel'




admin.site.register(Contact)
# admin.site.register(TruckFormData)


class Show_Non_commercial_auto_Form_Data(admin.ModelAdmin):
    # list_filter = ('date','reference')
    list_display = ('first_name','last_name', 'phone','email', 'company')
admin.site.register(NCAutoFormData, Show_Non_commercial_auto_Form_Data)

class Show_Commercial_Auto_Data(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'phone','email', 'driver_name')
admin.site.register(CAutoInsurance, Show_Commercial_Auto_Data)


class Show_Home_Form_Data(admin.ModelAdmin):
#     # list_filter = ('date','reference')
    list_display = ('first_name','last_name', 'phone','email')
admin.site.register(HomeInsuranceForm,Show_Home_Form_Data)


class Show_Life_Form_Data(admin.ModelAdmin):
#     # list_filter = ('date','reference')
    list_display = ('first_name','last_name', 'phone','email')
admin.site.register(LifeInsuranceForm,Show_Life_Form_Data)