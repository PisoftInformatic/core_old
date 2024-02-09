from django.db import models

# # Create your models here.



class WebsiteProfileData(models.Model):
    company_phone_number = models.CharField(max_length = 50)
    company_phone_number2 = models.CharField(max_length = 50)
    company_phone_number3 = models.CharField(max_length = 50)
    company_email_id = models.CharField(max_length=50)
    company_address = models.CharField(max_length = 100)
    def __str__(self):
        return self.company_phone_number or self.company_email_id or self.company_address
    class Meta:
        verbose_name_plural = "Website Profile Data"

class EmailConfig(models.Model):
    smtp_backend = models.CharField(max_length = 150, default='django.core.mail.backends.smtp.EmailBackend')
    smtp_server_name = models.CharField(max_length = 50)
    smtp_server_port = models.CharField(max_length = 30)
    email_address = models.CharField(max_length = 150)
    email_pasword = models.CharField(max_length = 50)
    use_tls = models.CharField(max_length=50)
    def __str__(self):
        return self.smtp_server_name or self.email_address
    class Meta:
        verbose_name_plural = "Email Configuration"