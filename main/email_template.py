from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def home_insurance_email(requests,fname, lname, dob,phone,email,address, cname,dot, mc, vmodel, vnumber ,vvalue):
    subject = f'New Entry on Website from {fname, lname} related to Home Insurance'
    message = f"""
    Hello Admin, 
    You Got 1 New Entry on DST Insurance Services.

    Client Name - {fname} {lname}
    Date Of Birth - {dob}
    Phone Number - {phone}
    Email - {email}
    Address - {address}
    Company - {cname}
    DOT = {dot}
    MC Number - {mc}
    Vehicle Model - {vmodel}
    Vehicle Number - {vnumber}
    Vehicle Value - {vvalue}

    These Are the Details Entered By The Client. 
    """
    
    from_email = 'dimpithakur2507@gmail.com'
    recipient_list = ['kuldeepsaini8865py@gmail.com']

    try:
        send_mail(subject=subject,message=message, from_email=from_email, recipient_list=recipient_list,
                  fail_silently=False,)
        messages.success(requests, 'Data Has Been Saved Successfuly!')
        return render(requests , 'quote/home-insurance-form.html')
    except Exception as e:
        messages.success(requests, f'Error Saving and sending email: {str(e)}')
        return render(requests , 'quote/home-insurance-form.html')
        # return (f'Error Saving and sending email: {str(e)}')
    
