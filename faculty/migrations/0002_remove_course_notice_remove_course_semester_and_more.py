# Generated by Django 4.1.7 on 2023-03-28 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='notice',
        ),
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
    ]
