# Generated by Django 2.2.24 on 2021-11-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_hide_disabled_flags'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='enable_dynamo_db',
            field=models.BooleanField(default=False, help_text='If true will fetch identity data(shown in the dashboard) from dynamodb'),
        ),
    ]
