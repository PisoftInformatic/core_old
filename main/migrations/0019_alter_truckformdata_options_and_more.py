# Generated by Django 4.2.7 on 2023-12-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_homeinsuranceform_client_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='truckformdata',
            options={},
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='day_phone',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='insurance_covered',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='msg',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='night_phone',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='truckformdata',
            name='send_text_on_phone',
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='address',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='dob',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='mc',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='phone',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='vehicle_model',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckformdata',
            name='vehicle_value',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
