# Generated by Django 4.2.7 on 2023-12-28 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_truckformdata_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truckformdata',
            old_name='text_permit',
            new_name='send_text_on_phone',
        ),
    ]
