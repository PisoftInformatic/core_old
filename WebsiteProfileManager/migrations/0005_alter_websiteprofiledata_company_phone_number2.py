# Generated by Django 5.0.1 on 2024-01-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteProfileManager', '0004_websiteprofiledata_company_phone_number2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteprofiledata',
            name='company_phone_number2',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]