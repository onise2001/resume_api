# Generated by Django 5.0.6 on 2024-06-25 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumes_api', '0002_remove_resume_experience_resume_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalinfo',
            name='image',
        ),
    ]
