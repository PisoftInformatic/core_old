from django.contrib import admin
from .models import *
# Register your models here.


class Website_Profile_Data(admin.ModelAdmin):
    list_display = ('company_phone_number','company_email_id')
admin.site.register(WebsiteProfileData, Website_Profile_Data)


class Email_Config_Data(admin.ModelAdmin):
    list_display = ('smtp_server_name','smtp_server_port', 'email_address')
admin.site.register(EmailConfig, Email_Config_Data)


