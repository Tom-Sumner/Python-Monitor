# Generated by Django 4.0.4 on 2023-06-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_employee_address_remove_employee_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailaccount',
            old_name='employee',
            new_name='owner',
        ),
    ]