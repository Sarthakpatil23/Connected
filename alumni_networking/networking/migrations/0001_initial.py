# Generated by Django 5.1.6 on 2025-02-19 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumniProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('graduation_year', models.CharField(choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029')], max_length=4)),
                ('current_job_title', models.CharField(max_length=255)),
                ('current_company', models.CharField(max_length=255)),
                ('industry', models.CharField(choices=[('Tech', 'Tech'), ('Finance', 'Finance'), ('Consulting', 'Consulting'), ('Marketing', 'Marketing')], max_length=50)),
                ('previous_companies', models.CharField(blank=True, max_length=500, null=True)),
                ('years_of_experience', models.CharField(choices=[('1-3', '1-3'), ('4-6', '4-6'), ('7-10', '7-10'), ('10+', '10+')], max_length=10)),
                ('willing_to_mentor', models.BooleanField(default=False)),
                ('number_of_mentees', models.CharField(blank=True, choices=[('1', '1'), ('3', '3'), ('5', '5'), ('Unlimited', 'Unlimited')], max_length=10, null=True)),
                ('preferred_mentorship_type', models.CharField(blank=True, choices=[('Career Guidance', 'Career Guidance'), ('Resume & Interview Prep', 'Resume & Interview Prep'), ('Startups & Entrepreneurship', 'Startups & Entrepreneurship'), ('Technical Skills & Projects', 'Technical Skills & Projects')], max_length=50, null=True)),
                ('preferred_communication_mode', models.CharField(blank=True, choices=[('Email', 'Email'), ('Platform Messaging', 'Platform Messaging'), ('Video Calls', 'Video Calls')], max_length=50, null=True)),
                ('availability', models.CharField(blank=True, choices=[('1-2 hours', '1-2 hours'), ('3-5 hours', '3-5 hours'), ('6+ hours', '6+ hours')], max_length=20, null=True)),
                ('post_jobs', models.BooleanField(default=False)),
                ('host_webinars', models.BooleanField(default=False)),
                ('topics_of_interest', models.CharField(blank=True, max_length=255, null=True)),
                ('receive_newsletter', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=255)),
                ('current_year_of_study', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('Graduate', 'Graduate')], max_length=10)),
                ('degree_program', models.CharField(choices=[('B.Tech', 'B.Tech'), ('BBA', 'BBA'), ('MBA', 'MBA'), ('M.Tech', 'M.Tech')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
