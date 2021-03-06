# Generated by Django 3.2 on 2022-02-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peopleadministration',
            name='project_experience',
            field=models.TextField(default='add experience', max_length=400),
        ),
        migrations.AlterField(
            model_name='peopletechsupport',
            name='project_experience',
            field=models.TextField(default='experience', max_length=400),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=150),
        ),
    ]
