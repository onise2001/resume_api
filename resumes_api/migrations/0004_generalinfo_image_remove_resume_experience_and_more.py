# Generated by Django 5.0.6 on 2024-06-25 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes_api', '0003_remove_generalinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalinfo',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='resume',
            name='experience',
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resumes_api.experience'),
            preserve_default=False,
        ),
    ]