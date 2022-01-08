# Generated by Django 4.0.1 on 2022-01-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_applicant_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='applicant',
        ),
        migrations.AddField(
            model_name='course',
            name='applicant',
            field=models.ManyToManyField(blank=True, null=True, to='schema.Applicant'),
        ),
    ]
