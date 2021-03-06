# Generated by Django 2.0.6 on 2018-06-05 16:12

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0016_auto_20170725_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdcuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='cdcuser',
            name='role',
            field=models.CharField(blank=True, choices=[('mentor', 'mentor'), ('guardian', 'guardian')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cdcuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, help_text='Basic HTML allowed', null=True),
        ),
        migrations.AlterField(
            model_name='emailcontent',
            name='body',
            field=models.TextField(blank=True, help_text='Basic HTML allowed', null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='condition',
            field=models.CharField(choices=[('working', 'Working'), ('issue', 'Issue'), ('unusable', 'Unusable')], max_length=255),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='force_update_on_next_boot',
            field=models.BooleanField(default=False, verbose_name='Force Update'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='last_system_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Update'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='last_system_update_check_in',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Check In'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='uuid',
            field=models.CharField(default='000-000-000-000', max_length=255, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address 2'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='additional_info',
            field=models.TextField(blank=True, help_text='Basic HTML allowed', null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='external_enrollment_url',
            field=models.CharField(blank=True, help_text='When provided, local enrollment is disabled.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='meetingtype',
            name='description',
            field=models.TextField(blank=True, help_text='Basic HTML allowed', null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='additional_info',
            field=models.TextField(blank=True, help_text='Basic HTML allowed', null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='session',
            name='external_enrollment_url',
            field=models.CharField(blank=True, help_text='When provided, local enrollment is disabled.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='gender_limitation',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Session is active.'),
        ),
        migrations.AlterField(
            model_name='session',
            name='is_public',
            field=models.BooleanField(default=False, help_text='Session is a public session.'),
        ),
        migrations.AlterField(
            model_name='student',
            name='consent',
            field=models.BooleanField(default=False, help_text='I hereby give consent for the student signed up above to participate in CoderDojoChi.', verbose_name='General Consent'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo_release',
            field=models.BooleanField(default=False, help_text="I hereby give permission to CoderDojoChi to use the student's image and/or likeness in promotional materials.", verbose_name='Photo Consent'),
        ),
    ]
