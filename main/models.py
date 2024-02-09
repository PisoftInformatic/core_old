from typing import Any
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name or self.email or self.phone
    class Meta:
        verbose_name_plural = "Contact Data"



class NCAutoFormData(models.Model):
    first_name =   models.CharField( max_length=50)
    last_name =   models.CharField( max_length=50)
    dob =   models.CharField( max_length=50)
    phone =   models.CharField( max_length=50)
    email =   models.CharField( max_length=50)
    address =   models.CharField( max_length=50)
    company =   models.CharField( max_length=50, blank = True, null = True)
    vehicle_model =   models.CharField( max_length=50)
    vehicle_number =   models.CharField( max_length=50)
    vehicle_value=   models.CharField( max_length=50)
    
    
    def __str__(self):
        return f'{self.first_name } {self.last_name}'

    class Meta:
        verbose_name_plural = "Non Commercial Auto Insurance Data"


class CAutoInsurance(models.Model):
    first_name =   models.CharField( max_length=50)
    last_name =   models.CharField( max_length=50)
    dob =   models.CharField( max_length=50)
    phone =   models.CharField( max_length=50)
    email =   models.CharField( max_length=50)
    address =   models.CharField( max_length=50)
    company =   models.CharField( max_length=50, blank = True, null = True)
    dot =   models.CharField( max_length=50, blank = True, null = True)
    mc =   models.CharField( max_length=50, blank = True, null = True)
    driver_name = models.CharField(max_length=50)
    license_no = models.CharField(max_length=50)
    vehicle_model =   models.CharField( max_length=50)
    vehicle_number =   models.CharField( max_length=50)
    vehicle_value=   models.CharField( max_length=50)
    
    
    def __str__(self):
        return f'{self.first_name } {self.last_name}'

    class Meta:
        verbose_name_plural = "Commercial Auto Insurance Data"



class HomeInsuranceForm(models.Model):
    first_name =   models.CharField( max_length=50)
    last_name =   models.CharField( max_length=50)
    dob =   models.CharField( max_length=50)
    phone =   models.CharField( max_length=50)
    email =   models.CharField( max_length=50)
    home_address =   models.CharField( max_length=50)
    pin_code =   models.CharField( max_length=50, blank = True, null = True)
    house_no =   models.CharField( max_length=50, blank = True, null = True)
    policy_number=   models.CharField( max_length=50, blank = True, null = True)
    house_area =   models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return f'{self.first_name } {self.last_name}'
    class Meta:
        verbose_name_plural = " Home Insurance Data"
    




class LifeInsuranceForm(models.Model):
    first_name =   models.CharField( max_length=50)
    last_name =   models.CharField( max_length=50)
    dob =   models.CharField( max_length=50)
    phone =   models.CharField( max_length=50)
    email =   models.CharField( max_length=50)
    details =   models.CharField( max_length=150, blank = True, null = True)
    gender =   models.CharField( max_length=50)
    # details = models.TextField()

    def __str__(self):
        return f'{self.first_name } {self.last_name}'
    class Meta:
        verbose_name_plural = " Life Insurance Data"
    