# Generated by Django 2.2.25 on 2022-01-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20210223_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='ffadminuser',
            name='marketing_consent_given',
            field=models.BooleanField(default=False, help_text='Determines whether the user has agreed to receive marketing mails'),
        ),
    ]
