# Generated by Django 4.2.7 on 2023-12-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_vechile_number_truckformdata_vehicle_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckformdata',
            name='date',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]