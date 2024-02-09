from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('services', services, name="services"),
    path('free-quote', freeQuote, name="free-quote"),
    path('insurance-services', insuranceServices, name="insurance-services"),

    # Services Urls
    path('ns-auto-insurance', ns_auto_insurance, name='ns-auto-insurance'),
    path('business-insurance', business_insurance, name='business-insurance'),
    path('home-auto-bundle', home_auto_bundle, name='home-auto-bundle'),
    path('engineering-insurance', engineering_insurance, name='engineering-insurance'),
    path('truck-insurance', truck_insurance, name='truck-insurance'),

    # Quote Urls
    # path('non-commercial-auto-form', non_commercial_auto_form, name='non-commercial-auto-form'),
    path('commercial-auto-form', CAuto_form, name='commercial-auto-form'),
    path('non-commercial-auto-form', NC_Auto_form, name='non-commercial-auto-form'),
    path('home-insurance-form', home_insurance_form, name='home-insurance-form'),
    path('life-insurance-form', life_insurance_form, name='life-insurance-form'),
   
]
