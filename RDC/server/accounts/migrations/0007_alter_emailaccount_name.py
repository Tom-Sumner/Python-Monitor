# Generated by Django 4.0.4 on 2023-06-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_emailaccount_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaccount',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
