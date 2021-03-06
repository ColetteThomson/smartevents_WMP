# Generated by Django 4.0 on 2022-02-01 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleAdministration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=120)),
                ('contact_no', models.CharField(blank=True, max_length=20)),
                ('person_email', models.EmailField(blank=True, max_length=254)),
                ('project_experience', models.TextField(default='experience', max_length=300)),
                ('ad_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='PeopleTechSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name_tech', models.CharField(max_length=120)),
                ('contact_no_tech', models.CharField(blank=True, max_length=20)),
                ('person_email_tech', models.EmailField(blank=True, max_length=254)),
                ('project_experience', models.TextField(default='experience', max_length=300)),
                ('ts_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=120)),
                ('project_date', models.DateTimeField()),
                ('description', models.TextField(max_length=300)),
                ('project_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
                ('resource_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.peopleadministration')),
                ('resource_tech', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.peopletechsupport')),
            ],
        ),
    ]
