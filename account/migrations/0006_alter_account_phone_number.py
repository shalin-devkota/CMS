# Generated by Django 4.1.7 on 2023-03-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
