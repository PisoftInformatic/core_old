# Generated by Django 5.0.1 on 2024-01-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteProfileManager', '0008_websiteprofiledata_company_phone_number3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websiteprofiledata',
            name='company_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
