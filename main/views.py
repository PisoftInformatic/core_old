from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from datetime import date
from .email_template import *
# Create your views here.

from WebsiteProfileManager.models import *
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image, Spacer
from django.http import HttpResponse
from io import BytesIO
from django.core.mail import get_connection
from django.shortcuts import render


# Get data from the model
profile_data = WebsiteProfileData.objects.all()
# phone1 = profile_data.company_phone_number
# phone2 = profile_data.company_phone_number2
# phone3 = profile_data.company_phone_number3

# # address1 = profile_data.company_address_line_1
# # address2 = profile_data.company_address_line_2
# # address3 = profile_data.company_address_line_3


# company_email = profile_data.company_email_id
# company_zip_code = profile_data.zip_code

company_address = [ 'DTS Insurance Services Inc.',
                   '3380 W Ashlan Ave',
                   'FRESNO, CA',
                   'Zip Code - 93722',
                   'Phone : 559-554-9835',
                   'Email : damandeep@dtsinsservices.com',
                ]

# Path Of the Logo of Pdf File -->
logo_path = 'E:/Kuldeep(Python)/Development/INsurance/core/static/img/logo1.png'
#logo_path = '/root/pypro/core/static/img/logo1.png'

# recipient_list = ['kuldeepsaini8865py@gmail.com', 'damandeep@dtsinsservices.com', 'Anjupisoft@gmail.com']
recipient_list = ['kuldeepsaini8865py@gmail.com','coolboyk.deepsaini@gmail.com']

email_config = EmailConfig.objects.first()
terms = '"Our insurance services cover a wide range of incidents, including but not limited to accidents, natural calamities, and unforeseen circumstances, subject to the terms outlined in this policy."'
terms2 = '"We prioritize safeguarding your privacy. Personal information collected during the insurance application process will be used solely for the purpose of providing insurance services and will not be shared without your consent, except as required by law."'
terms3 = '" By availing of our insurance services, you acknowledge and agree that accurate and truthful information provided in the application process is crucial for policy validity and claim processing. "'
terms4 = '" The insurance provider reserves the right to modify policy terms and conditions with proper notice. Modifications may be made to comply with regulations or enhance policy offerings."'



def home(requests):
    return render(requests, 'index.html')

def about(requests):
    return render(requests, 'about.html')

def contact(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        msg = requests.POST.get('msg')

        # Saving Data to the DataBase
        data = Contact(name=name, phone=phone, email=email, message=msg)
        data.save()

        # Sending Data to Mail
        subject = f'New Contact Entry from {name}.'

        # Use triple quotes for multi-line string
        message = f"""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Contact Form Entry</title>
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                    }}

                    .container {{
                        max-width: 600px;
                        margin: 50px auto;
                        padding: 20px;
                        background-color: #fff;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        border-radius: 5px;
                    }}

                    header {{
                        background-color: #3498db;
                        color: #fff;
                        text-align: center;
                        padding: 20px;
                    }}

                    section {{
                        padding: 20px;
                    }}

                    footer {{
                        background-color: #f2f2f2;
                        text-align: center;
                        padding: 10px;
                    }}

                    ul {{
                        list-style-type: none;
                        padding: 0;
                    }}

                    li {{
                        margin-bottom: 10px;
                    }}

                    h2 {{
                        color: #333;
                    }}

                    p {{
                        margin-bottom: 15px;
                        line-height: 1.6;
                    }}
                </style>
            </head>

            <body>
                <div class="container">
                    <header>
                        <h2>New Data Received in Contact Form </h2>
                    </header>
                    <section>
                        <p>Dear Admin,</p>
                        <p>You have received a new contact form entry. Details are as follows:</p>
                        <ul>
                            <li><strong>Name:</strong> { name }</li>
                            <li><strong>Email:</strong> { email }</li>
                            <li><strong>Phone:</strong> { phone }</li>
                            <li><strong>Message:</strong> { msg }</li>
                        </ul>
                        <p>Thank you for your attention.</p>
                        <p>Best regards,</p>
                    </section>
                    <footer>
                        <p>This is an automated email. Please do not reply to this email.</p>
                    </footer>
                </div>
            </body>

            </html> """


        email_config = EmailConfig.objects.first()

        # email_config = EmailConfig.objects.first()
        email = EmailMessage(
                subject=subject,
                body=message,
                from_email=email_config.email_address,
                to=recipient_list,
                reply_to=[email_config.email_address],
            )

        email.content_subtype = 'html'  # Set content type to HTML

            # Set the backend and connection details
        connection = get_connection(
                backend=email_config.smtp_backend,
                host=email_config.smtp_server_name,
                port=email_config.smtp_server_port,
                username=email_config.email_address,
                password=email_config.email_pasword,
                use_tls=email_config.use_tls.lower() == 'true',
            )
        email.connection = connection

            # Send the email
        email.send()

        messages.success(requests, 'Data Has Been Saved Successfully!')
        return redirect('contact')

    return render(requests, 'contact.html', {'sitedata':profile_data})


def services(requests):
    return render(requests, 'services.html')

def freeQuote(requests):
    return render(requests, 'free-quote.html')

def insuranceServices(requests):
    return render(requests, 'services/insurance-services.html')

# Services Insurance
def ns_auto_insurance(requests):
    return render(requests, 'services/ns-auto-insurance.html')

def business_insurance(requests):
    return render(requests, 'services/business-insurance.html')

def home_auto_bundle(requests):
    return render(requests, 'services/home-auto-bundle.html')

def engineering_insurance(requests):
    return render(requests, 'services/engineering-insurance.html')

def truck_insurance(requests):
    return render(requests, 'services/truck-insurance.html')


# Quote

def truck_form(requests):
    return render(requests, 'quote/truck-form.html')


def CAuto_form(requests):
    if requests.method == 'POST':
        buffer = BytesIO()

        user_info = {
            'fname' : requests.POST.get('fname'),
            'lname' : requests.POST.get('lname'),
            'dob' : requests.POST.get('dob'),
            'phone' : requests.POST.get('phone'),
            'email' : requests.POST.get('email'),
            'address' : requests.POST.get('address'),
            'cname' : requests.POST.get('cname'),
            'dot' : requests.POST.get('dot'),
            'mc' : requests.POST.get('mc'),
            'drivername' : requests.POST.get('drivername'),
            'license_no' : requests.POST.get('license_no'),
            'vnumber' : requests.POST.get('vnumber'),
            'vvalue' : requests.POST.get('vvalue'),
            'vmodel' : requests.POST.get('vmodel'),
        }

        # Data for the user information table
        user_data = [
            ['Full Name:', f"{user_info.get('fname', '')} {user_info.get('lname', '')}"],
            ['DOB:', user_info.get('dob', '')],
            ['Phone:', user_info.get('phone', '')],
            ['Email:', user_info.get('email', '')],
            ['Address:', user_info.get('address', '')],
            ['Company Name:', user_info.get('cname', '')],
            ['DOT Number', user_info.get('dot', '')],
            ['MC Number:', user_info.get('mc', '')],
            ['Driver Name:', user_info.get('drivername', '')],
            ['License Number:', user_info.get('license_no', '')],
            ['Vehicle Number:', user_info.get('vnumber', '')],
            ['Vehicle Value:', user_info.get('vvalue', '')],
            ['Vehicle Model:', user_info.get('vmodel', '')],
        #   ['Details:', Paragraph(user_info.get('Details', ''), ParagraphStyle('DetailsStyle', fontSize=12, leading=16))],
        ]
        # Set up the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=40)
        logo = Image(logo_path, width=100, height=70)

        # Company address as a list of lines

        # Create the company header table
        company_table = Table([
            [logo, '\n'.join(company_address)],
            ['', ''],  # Display address lines one below the other
        ], colWidths=[250, 250])

        # Add style to the company header table
        company_style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),  # Align the address to the top
            ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),  # Align the logo to the middle
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ])

        company_table.setStyle(company_style)

        # Create the user information table
        user_table = Table(user_data, colWidths=[150, 300])

        # Add style to the user information table
        user_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        user_table.setStyle(user_style)

        # heading
        heading_style = ParagraphStyle('Heading1', parent=getSampleStyleSheet()['Title'], fontSize=18, spaceBefore=30, spaceAfter=10, alignment=1)
        heading = Paragraph('Client Details  for Commercial Auto Insurance Quote', heading_style)

        # Terms And contitions
        # heading
        ters_heading_style = ParagraphStyle('termsheading', parent=getSampleStyleSheet()['Title'], fontSize=13, spaceBefore=20, spaceAfter=0, alignment=0)
        ters_heading_line = Paragraph('Terms And Conditions*', ters_heading_style)
        termsconditions_style = ParagraphStyle('termsconditions', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=0, spaceAfter=5, alignment=0)
        termsconditions_line = Paragraph(terms, termsconditions_style)
        termsconditions_style2 = ParagraphStyle('termsconditions2', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=5, spaceAfter=5, alignment=0)
        termsconditions_line2 = Paragraph(terms2, termsconditions_style2)
        termsconditions_line3 = Paragraph(terms3, termsconditions_style2)
        termsconditions_line4 = Paragraph(terms4, termsconditions_style2)

        # Signature
        signature_style = ParagraphStyle('Signature', parent=getSampleStyleSheet()['Title'], fontSize=12, spaceBefore=30, spaceAfter=0, alignment=2)
        signature_line = Paragraph('Authorized  Signature', signature_style)



        # Build the PDF document with all elements
        doc.build([company_table, heading, user_table,ters_heading_line,termsconditions_line, termsconditions_line2,termsconditions_line3,termsconditions_line4, signature_line])


        # Storing the PDF in the file Variable
        file = buffer.getvalue()

        subject = 'Client Commercial Auto Insurance Policy Details'

        html_message = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Insurance Policy Details</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                line-height: 1.6;
                                margin: 0;
                                padding: 0;
                            }}

                            header {{
                                background-color: #3498db;
                                color: #fff;
                                text-align: center;
                                padding: 20px;
                            }}

                            section {{
                                padding: 20px;
                            }}

                            footer {{
                                background-color: #f2f2f2;
                                text-align: center;
                                padding: 10px;
                            }}
                        </style>
                    </head>
                    <body>
                        <header>
                            <h1>Commercial Auto Insurance Client Details</h1>
                        </header>

                        <section>
                            <p>Dear DTS Admin,</p>

                            <p>You Got One more New Data for Commercial Auto Insurance Quote. Details Are mentiond below  </p>

                            <ul>
                                <li><strong>Name:</strong> {user_info.get('fname', '')} {user_info.get('lname', '')}</li>
                                <li><strong>DOB :</strong> {user_info.get('dob', '')}</li>
                                <li><strong>Phone:</strong> {user_info.get('phone', '')}</li>
                                <li><strong>Email:</strong> {user_info.get('email', '')}</li>
                                <li><strong>Address:</strong> {user_info.get('address', '')}</li>
                                <li><strong>Company Name :</strong> {user_info.get('cname', '')}</li>
                                <li><strong>MC Number :</strong> {user_info.get('mc', '')}</li>
                                <li><strong>DOT Number :</strong> {user_info.get('dot', '')}</li>
                                <li><strong>Driver Name :</strong> {user_info.get('drivername', '')}</li>
                                <li><strong>License Number :</strong> {user_info.get('license_no', '')}</li>
                                <li><strong>Vehicle Number :</strong> {user_info.get('vnumber', '')}</li>
                                <li><strong>Vehicle Value :</strong> {user_info.get('vvalue', '')}</li>
                                <li><strong>Vehicle Model :</strong> {user_info.get('vmodel', '')}</li>
                                <!-- Include other relevant details -->
                            </ul>

                            <p>These Details Are also mentioned in the pdf file. Make sure to check the Given attechment file.</p>

                            <p>Best regards</p>
                        </section>

                        <footer>
                            <p>This is an automated email. Please do not reply to this email.</p>
                        </footer>
                    </body>
                    </html>
                """



        try:

            email = EmailMessage(
                subject=subject,
                body='',
                from_email=email_config.email_address,
                to=recipient_list,
                reply_to=[email_config.email_address],
            )

            email.content_subtype = 'html'  # Set content type to HTML

            # Set the backend and connection details
            connection = get_connection(
                backend=email_config.smtp_backend,
                host=email_config.smtp_server_name,
                port=email_config.smtp_server_port,
                username=email_config.email_address,
                password=email_config.email_pasword,
                use_tls=email_config.use_tls.lower() == 'true',
            )

            # Assign the connection to the EmailMessage instance

            # Attach the PDF file
            email.attach('Insurance_Policy_Details.pdf', file, 'application/pdf')
            email.content_subtype = 'html'

            email.connection = connection
            # Set the HTML message in the body
            email.body = html_message
            email.send()

            # Saving data to Database
            save_data = CAutoInsurance(
               first_name=user_info['fname'],
               last_name=user_info['lname'],
               dob=user_info['dob'],
               phone=user_info['phone'],
               email=user_info['email'],
               address=user_info['address'],
               company=user_info['cname'],
               dot=user_info['dot'],
               mc=user_info['mc'],
               driver_name=user_info['drivername'],
               license_no=user_info['license_no'],
               vehicle_model=user_info['vmodel'],
               vehicle_number=user_info['vnumber'],
               vehicle_value=user_info['vvalue'],
               )
            save_data.save()
            messages.success(requests, 'Data Has Been Saved Successfully!')
            return redirect('commercial-auto-form')

        except Exception as e:
            messages.error(requests, f'Error Saving and sending email: {str(e)}')
            return redirect('commercial-auto-form')



    return render(requests, 'quote/commercial-auto-form.html')

def NC_Auto_form(requests):
    if requests.method == 'POST':
        buffer = BytesIO()

        user_info = {
            'fname' : requests.POST.get('fname'),
            'lname' : requests.POST.get('lname'),
            'dob' : requests.POST.get('dob'),
            'phone' : requests.POST.get('phone'),
            'email' : requests.POST.get('email'),
            'address' : requests.POST.get('address'),
            'cname' : requests.POST.get('cname'),
            'vnumber' : requests.POST.get('vnumber'),
            'vvalue' : requests.POST.get('vvalue'),
            'vmodel' : requests.POST.get('vmodel'),
        }

        # Data for the user information table
        user_data = [
            ['Full Name:', f"{user_info.get('fname', '')} {user_info.get('lname', '')}"],
            ['DOB:', user_info.get('dob', '')],
            ['Phone:', user_info.get('phone', '')],
            ['Email:', user_info.get('email', '')],
            ['Address:', user_info.get('address', '')],
            ['Company Name:', user_info.get('cname', '')],
            ['Vehicle Number:', user_info.get('vnumber', '')],
            ['Vehicle Value:', user_info.get('vvalue', '')],
            ['Vehicle Model:', user_info.get('vmodel', '')],
        #   ['Details:', Paragraph(user_info.get('Details', ''), ParagraphStyle('DetailsStyle', fontSize=12, leading=16))],
        ]
        # Set up the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=40)
        logo = Image(logo_path, width=100, height=70)


        # Create the company header table
        company_table = Table([
            [logo, '\n'.join(company_address)],
            ['', ''],  # Display address lines one below the other
        ], colWidths=[250, 250])

        # Add style to the company header table
        company_style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),  # Align the address to the top
            ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),  # Align the logo to the middle
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ])

        company_table.setStyle(company_style)

        # Create the user information table
        user_table = Table(user_data, colWidths=[150, 300])

        # Add style to the user information table
        user_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        user_table.setStyle(user_style)

        # heading
        heading_style = ParagraphStyle('Heading1', parent=getSampleStyleSheet()['Title'], fontSize=18, spaceBefore=30, spaceAfter=10, alignment=1)
        heading = Paragraph('Client Details  for Non Commercial Auto Insurance Quote', heading_style)

        # Terms And contitions
        # heading
        ters_heading_style = ParagraphStyle('termsheading', parent=getSampleStyleSheet()['Title'], fontSize=13, spaceBefore=50, spaceAfter=0, alignment=0)
        ters_heading_line = Paragraph('Terms And Conditions*', ters_heading_style)
        termsconditions_style = ParagraphStyle('termsconditions', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=0, spaceAfter=5, alignment=0)
        termsconditions_line = Paragraph(terms, termsconditions_style)
        termsconditions_style2 = ParagraphStyle('termsconditions2', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=5, spaceAfter=5, alignment=0)
        termsconditions_line2 = Paragraph(terms2, termsconditions_style2)
        termsconditions_line3 = Paragraph(terms3, termsconditions_style2)
        termsconditions_line4 = Paragraph(terms4, termsconditions_style2)

        # Signature
        signature_style = ParagraphStyle('Signature', parent=getSampleStyleSheet()['Title'], fontSize=12, spaceBefore=60, spaceAfter=0, alignment=2)
        signature_line = Paragraph('Authorized  Signature', signature_style)



        # Build the PDF document with all elements
        doc.build([company_table, heading, user_table,ters_heading_line,termsconditions_line, termsconditions_line2,termsconditions_line3,termsconditions_line4, signature_line])


        # Storing the PDF in the file Variable
        file = buffer.getvalue()

        subject = 'Non Commercial Auto Insurance Details'

        html_message = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Non Commercial Insurance Policy Details</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                line-height: 1.6;
                                margin: 0;
                                padding: 0;
                            }}

                            header {{
                                background-color: #3498db;
                                color: #fff;
                                text-align: center;
                                padding: 20px;
                            }}

                            section {{
                                padding: 20px;
                            }}

                            footer {{
                                background-color: #f2f2f2;
                                text-align: center;
                                padding: 10px;
                            }}
                        </style>
                    </head>
                    <body>
                        <header>
                            <h1>Non Commercial Auto Insurance Client Details</h1>
                        </header>

                        <section>
                            <p>Dear DTS Admin,</p>

                            <p>You Got One more New Data for Non Commercial Auto Insurance Quote. Details Are mentiond below  </p>

                            <ul>
                                <li><strong>Name:</strong> {user_info.get('fname', '')} {user_info.get('lname', '')}</li>
                                <li><strong>DOB :</strong> {user_info.get('dob', '')}</li>
                                <li><strong>Phone:</strong> {user_info.get('phone', '')}</li>
                                <li><strong>Email:</strong> {user_info.get('email', '')}</li>
                                <li><strong>Address:</strong> {user_info.get('address', '')}</li>
                                <li><strong>Company Name :</strong> {user_info.get('cname', '')}</li>
                                <li><strong>Vehicle Number :</strong> {user_info.get('vnumber', '')}</li>
                                <li><strong>Vehicle Value :</strong> {user_info.get('vvalue', '')}</li>
                                <li><strong>Vehicle Model :</strong> {user_info.get('vmodel', '')}</li>
                                <!-- Include other relevant details -->
                            </ul>

                            <p>These Details Are also mentioned in the pdf file. Make sure to check the Given attechment file.</p>

                            <p>Best regards</p>
                        </section>

                        <footer>
                            <p>This is an automated email. Please do not reply to this email.</p>
                        </footer>
                    </body>
                    </html>
                """



        try:

            email = EmailMessage(
                subject=subject,
                body='',
                from_email=email_config.email_address,
                to=recipient_list,
                reply_to=[email_config.email_address],
            )

            email.content_subtype = 'html'  # Set content type to HTML

            # Set the backend and connection details
            connection = get_connection(
                backend=email_config.smtp_backend,
                host=email_config.smtp_server_name,
                port=email_config.smtp_server_port,
                username=email_config.email_address,
                password=email_config.email_pasword,
                use_tls=email_config.use_tls.lower() == 'true',
            )

            # Assign the connection to the EmailMessage instance

            # Attach the PDF file
            email.attach('Non-Commercial-Auto-Insurance.pdf', file, 'application/pdf')
            email.content_subtype = 'html'

            email.connection = connection
            # Set the HTML message in the body
            email.body = html_message
            email.send()

            # Saving data to Database
            save_data = CAutoInsurance(
               first_name=user_info['fname'],
               last_name=user_info['lname'],
               dob=user_info['dob'],
               phone=user_info['phone'],
               email=user_info['email'],
               address=user_info['address'],
               company=user_info['cname'],
               vehicle_model=user_info['vmodel'],
               vehicle_number=user_info['vnumber'],
               vehicle_value=user_info['vvalue'],
               )
            save_data.save()
            messages.success(requests, 'Data Has Been Saved Successfully!')
            return redirect('non-commercial-auto-form')

        except Exception as e:
            messages.error(requests, f'Error Saving and sending email: {str(e)}')
            return redirect('non-commercial-auto-form')



    return render(requests, 'quote/non-commercial-auto-form.html')


def home_insurance_form(requests):
    if requests.method == 'POST':
        buffer = BytesIO()
        user_info = {
            'fname' : requests.POST.get('fname'),
            'lname' : requests.POST.get('lname'),
            'dob' : requests.POST.get('dob'),
            'phone' : requests.POST.get('phone'),
            'email' : requests.POST.get('email'),
            'address' : requests.POST.get('address'),
            'pin_code' : requests.POST.get('pincode'),
            'house_no' : requests.POST.get('houseno'),
            'house_area' : requests.POST.get('housearea'),
            'policy_number' : requests.POST.get('pnumber'),
        }
        home_insurance_form_instance = HomeInsuranceForm(
        first_name=user_info['fname'],
        last_name=user_info['lname'],
        dob=user_info['dob'],
        phone=user_info['phone'],
        email=user_info['email'],
        home_address=user_info['address'],
        pin_code=user_info['pin_code'],
        house_no=user_info['house_no'],
        house_area=user_info['house_area'],
        policy_number=user_info['policy_number'],
)

# Save the instance to the database
        home_insurance_form_instance.save()


        # Data for the user information table
        user_data = [
            ['Full Name:', f"{user_info.get('fname', '')} {user_info.get('lname', '')}"],
            ['DOB:', user_info.get('dob', '')],
            ['Phone:', user_info.get('phone', '')],
            ['Email:', user_info.get('email', '')],
            ['Address:', user_info.get('address', '')],
            ['Pin Code:', user_info.get('pin_code', '')],
            ['House Number', user_info.get('house_no', '')],
            ['House Area Covered (ft.):', user_info.get('house_area', '')],
            ['Policy Number:', user_info.get('policy_number', '')],
        #   ['Details:', Paragraph(user_info.get('Details', ''), ParagraphStyle('DetailsStyle', fontSize=12, leading=16))],
        ]
        # Set up the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=40)
        logo = Image(logo_path, width=100, height=70)

        # Create the company header table
        company_table = Table([
            [logo, '\n'.join(company_address)],
            ['', ''],  # Display address lines one below the other
        ], colWidths=[250, 250])

        # Add style to the company header table
        company_style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),  # Align the address to the top
            ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),  # Align the logo to the middle
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ])

        company_table.setStyle(company_style)

        # Create the user information table
        user_table = Table(user_data, colWidths=[150, 300])

        # Add style to the user information table
        user_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        user_table.setStyle(user_style)

        # heading
        heading_style = ParagraphStyle('Heading1', parent=getSampleStyleSheet()['Title'], fontSize=18, spaceBefore=30, spaceAfter=10, alignment=1)
        heading = Paragraph('Client Details for Home Insurance Quote', heading_style)

        # Terms And contitions
        # heading
        ters_heading_style = ParagraphStyle('termsheading', parent=getSampleStyleSheet()['Title'], fontSize=13, spaceBefore=70, spaceAfter=0, alignment=0)
        ters_heading_line = Paragraph('Terms And Conditions*', ters_heading_style)
        termsconditions_style = ParagraphStyle('termsconditions', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=0, spaceAfter=5, alignment=0)
        termsconditions_line = Paragraph(terms, termsconditions_style)
        termsconditions_style2 = ParagraphStyle('termsconditions2', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=5, spaceAfter=5, alignment=0)
        termsconditions_line2 = Paragraph(terms2, termsconditions_style2)
        termsconditions_line3 = Paragraph(terms3, termsconditions_style2)
        termsconditions_line4 = Paragraph(terms4, termsconditions_style2)

        # Signature
        signature_style = ParagraphStyle('Signature', parent=getSampleStyleSheet()['Title'], fontSize=12, spaceBefore=70, spaceAfter=0, alignment=2)
        signature_line = Paragraph('Authorized  Signature', signature_style)



        # Build the PDF document with all elements
        doc.build([company_table, heading, user_table,ters_heading_line,termsconditions_line, termsconditions_line2,termsconditions_line3,termsconditions_line4, signature_line])


        # Storing the PDF in the file Variable
        file = buffer.getvalue()

        subject = 'New Data received from client "Home Insurance"'

        html_message = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Insurance Policy Details</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                line-height: 1.6;
                                margin: 0;
                                padding: 0;
                            }}

                            header {{
                                background-color: #3498db;
                                color: #fff;
                                text-align: center;
                                padding: 20px;
                            }}

                            section {{
                                padding: 20px;
                            }}

                            footer {{
                                background-color: #f2f2f2;
                                text-align: center;
                                padding: 10px;
                            }}
                        </style>
                    </head>
                    <body>
                        <header>
                            <h1>Home Insurance Customer Details</h1>
                        </header>

                        <section>
                            <p>Dear DTS Admin,</p>

                            <p>You Got One more New Data for Home Insurance Service. Details Are mentiond below  </p>

                            <ul>
                                <li><strong>Name:</strong> {user_info.get('fname', '')} {user_info.get('lname', '')}</li>
                                <li><strong>DOB :</strong> {user_info.get('dob', '')}</li>
                                <li><strong>Phone:</strong> {user_info.get('phone', '')}</li>
                                <li><strong>Email:</strong> {user_info.get('email', '')}</li>
                                <li><strong>Address:</strong> {user_info.get('address', '')}</li>
                                <li><strong>Pin Code :</strong> {user_info.get('pin_code', '')}</li>
                                <li><strong>House No :</strong> {user_info.get('house_no', '')}</li>
                                <li><strong>House Area Covered (ft):</strong> {user_info.get('house_area', '')}</li>
                                <li><strong>Policy Number :</strong> {user_info.get('policy_number', '')}</li>
                                <!-- Include other relevant details -->
                            </ul>

                            <p>These Details Are also mentioned in the pdf file. Make sure to check the Given attechment file.</p>

                            <p>Best regards</p>
                        </section>

                        <footer>
                            <p>This is an automated email. Please do not reply to this email.</p>
                        </footer>
                    </body>
                    </html>
                """


        try:

            email = EmailMessage(
                subject=subject,
                body='',
                from_email=email_config.email_address,
                to=recipient_list,
                reply_to=[email_config.email_address],
            )

            email.content_subtype = 'html'  # Set content type to HTML

            # Set the backend and connection details
            connection = get_connection(
                backend=email_config.smtp_backend,
                host=email_config.smtp_server_name,
                port=email_config.smtp_server_port,
                username=email_config.email_address,
                password=email_config.email_pasword,
                use_tls=email_config.use_tls.lower() == 'true',
            )

            # Assign the connection to the EmailMessage instance

            # Attach the PDF file
            email.attach('Insurance_Policy_Details.pdf', file, 'application/pdf')
            email.content_subtype = 'html'

            email.connection = connection
            # Set the HTML message in the body
            email.body = html_message
            email.send()

            messages.success(requests, 'Data Has Been Saved Successfully!')
            return redirect('home-insurance-form')

        except Exception as e:
            messages.error(requests, f'Error Saving and sending email: {str(e)}')
            return redirect('home-insurance-form')



    return render(requests, 'quote/home-insurance-form.html')



def life_insurance_form(requests):
    if requests.method == 'POST':
        buffer = BytesIO()
        user_info = {
            'FName': requests.POST.get('fname'),
            'LName': requests.POST.get('lname'),
            'DOB': requests.POST.get('dob'),
            'Gender': requests.POST.get('gender'),
            'Phone': requests.POST.get('phone'),
            'Email': requests.POST.get('email'),
            'Details': requests.POST.get('details'),
        }

        life_insurance_form_instance = LifeInsuranceForm(
        first_name=user_info['FName'],
        last_name=user_info['LName'],
        dob=user_info['DOB'],
        phone=user_info['Phone'],
        email=user_info['Email'],
        details=user_info['Details'],
        gender=user_info['Gender'],
         )

        # Save the instance to the database
        life_insurance_form_instance.save()

        # Data for the user information table
        user_data = [
            ['Name:', f"{user_info.get('FName', '')} {user_info.get('LName', '')} "],
            ['DOB:', user_info.get('DOB', '')],
            ['Phone:', user_info.get('Phone', '')],
            ['Email:', user_info.get('Email', '')],
            ['Gender:', user_info.get('Gender', '')],
          ['Details:', Paragraph(user_info.get('Details', ''), ParagraphStyle('DetailsStyle', fontSize=12, leading=16))],
        ]

        # Set up the PDF document
        doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=40)

        # Load the company logo image
        logo = Image(logo_path, width=100, height=70)

        # Create the company header table
        company_table = Table([
            [logo, '\n'.join(company_address)],
            ['', ''],  # Display address lines one below the other
        ], colWidths=[250, 250])

        # Add style to the company header table
        company_style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (1, -1), 'RIGHT'),  # Align the address to the top
            ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),  # Align the logo to the middle
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ])

        company_table.setStyle(company_style)

        # heading
        heading_style = ParagraphStyle('Heading1', parent=getSampleStyleSheet()['Title'], fontSize=18, spaceBefore=30, spaceAfter=10, alignment=1)
        heading = Paragraph('Client Details for Life Insurance Quote', heading_style)

        # Terms And contitions
        # heading
        ters_heading_style = ParagraphStyle('termsheading', parent=getSampleStyleSheet()['Title'], fontSize=13, spaceBefore=70, spaceAfter=0, alignment=0)
        ters_heading_line = Paragraph('Terms And Conditions*', ters_heading_style)
        termsconditions_style = ParagraphStyle('termsconditions', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=0, spaceAfter=5, alignment=0)
        termsconditions_line = Paragraph(terms, termsconditions_style)
        termsconditions_style2 = ParagraphStyle('termsconditions2', parent=getSampleStyleSheet()['Normal'], fontSize=10, spaceBefore=5, spaceAfter=5, alignment=0)
        termsconditions_line2 = Paragraph(terms2, termsconditions_style2)
        termsconditions_line3 = Paragraph(terms3, termsconditions_style2)
        termsconditions_line4 = Paragraph(terms4, termsconditions_style2)

        # Signature
        signature_style = ParagraphStyle('Signature', parent=getSampleStyleSheet()['Title'], fontSize=12, spaceBefore=140, spaceAfter=0, alignment=2)
        signature_line = Paragraph('Authorized  Signature', signature_style)

        # Create the user information table
        user_table = Table(user_data, colWidths=[100, 300])

        # Add style to the user information table
        user_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        user_table.setStyle(user_style)

        # Build the PDF document with all elements
        doc.build([company_table, heading, user_table,ters_heading_line,termsconditions_line, termsconditions_line2,termsconditions_line3,termsconditions_line4, signature_line])

        buffer.seek(0)

        # Storing the PDF in the file Variable
        file = buffer.getvalue()

        subject = 'Client Details for Home Insurance Quote'

        html_message = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Insurance Policy Details</title>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                line-height: 1.6;
                                margin: 0;
                                padding: 0;
                            }}

                            header {{
                                background-color: #3498db;
                                color: #fff;
                                text-align: center;
                                padding: 20px;
                            }}

                            section {{
                                padding: 20px;
                            }}

                            footer {{
                                background-color: #f2f2f2;
                                text-align: center;
                                padding: 10px;
                            }}
                        </style>
                    </head>
                    <body>
                        <header>
                            <h1>Life Insurance Customer Details</h1>
                        </header>

                        <section>
                            <p>Dear DTS Admin,</p>

                            <p>You Got One more New Data for Life Insurance Service. Details Are mentiond below and dont forget to check pdf attachment </p>

                            <ul>
                                <li><strong>Name:</strong> {user_info.get('FName', '')} {user_info.get('LName', '')}</li>
                                <li><strong>DOB:</strong> {user_info.get('DOB', '')}</li>
                                <li><strong>Gender:</strong> {user_info.get('Gender', '')}</li>
                                <li><strong>Phone:</strong> {user_info.get('Phone', '')}</li>
                                <li><strong>Email:</strong> {user_info.get('Email', '')}</li>
                                <!-- Include other relevant details -->
                            </ul>

                            <p>Best regards</p>
                        </section>

                        <footer>
                            <p>This is an automated email. Please do not reply to this email.</p>
                        </footer>
                    </body>
                    </html>
                """



        try:

            email = EmailMessage(
                subject=subject,
                body='',
                from_email=email_config.email_address,
                to=recipient_list,
                reply_to=[email_config.email_address],
            )

            email.content_subtype = 'html'  # Set content type to HTML

            # Set the backend and connection details
            connection = get_connection(
                backend=email_config.smtp_backend,
                host=email_config.smtp_server_name,
                port=email_config.smtp_server_port,
                username=email_config.email_address,
                password=email_config.email_pasword,
                use_tls=email_config.use_tls.lower() == 'true',
            )

            # Assign the connection to the EmailMessage instance

            # Attach the PDF file
            email.attach('Insurance_Policy_Details.pdf', file, 'application/pdf')
            email.content_subtype = 'html'

            email.connection = connection
            # Set the HTML message in the body
            email.body = html_message
            email.send()

            messages.success(requests, 'Data Has Been Saved Successfully! ')
            return redirect('life-insurance-form')

        except Exception as e:
            messages.error(requests, f'Error Saving and sending email: {str(e)}')
            return redirect('life-insurance-form')



    return render(requests, 'quote/life-insurance-form.html')