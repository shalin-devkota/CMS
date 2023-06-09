# Generated by Django 4.1.7 on 2023-04-21 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0009_alter_subject_notice"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("deadline", models.DateField()),
                ("assignment_file", models.FileField(upload_to="")),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="faculty.subject",
                    ),
                ),
            ],
        ),
    ]
