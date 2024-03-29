# Generated by Django 4.2.7 on 2024-01-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_server_name', models.CharField(max_length=50)),
                ('smtp_server_port', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=150)),
                ('email_pasword', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Email Configuration',
            },
        ),
        migrations.CreateModel(
            name='WebsiteProfileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_phone_number', models.CharField(max_length=50)),
                ('company_email_id', models.CharField(max_length=50)),
                ('company_address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Website Profile Data',
            },
        ),
    ]
