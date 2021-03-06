# Generated by Django 4.0.1 on 2022-01-08 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0006_remove_course_applicant_applicant_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='schema.tutor'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='course',
            field=models.ManyToManyField(blank=True, to='schema.Course'),
        ),
    ]
