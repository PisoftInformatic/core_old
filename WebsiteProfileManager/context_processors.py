from .models import *  # Import your model representing company information

def footer_data(request):
    try:
        company_info = WebsiteProfileData.objects.first()  # Fetch the company information from your database
    except WebsiteProfileData.DoesNotExist:
        company_info = None

    return {
        'company_info': company_info,
    }