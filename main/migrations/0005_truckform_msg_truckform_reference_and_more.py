# Generated by Django 4.2.7 on 2023-12-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_name_truckform_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckform',
            name='msg',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckform',
            name='reference',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckform',
            name='text_permit',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truckform',
            name='vechile_number',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
