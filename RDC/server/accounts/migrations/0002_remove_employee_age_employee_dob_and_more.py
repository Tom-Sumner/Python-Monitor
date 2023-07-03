# Generated by Django 4.0.4 on 2023-06-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateField(default='2007-07-11', verbose_name='Date of Birth'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailaccount',
            name='password',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]