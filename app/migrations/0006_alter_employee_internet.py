# Generated by Django 4.1.2 on 2022-12-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_employee_internet_employee_shares_access_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='internet',
            field=models.CharField(choices=[(True, 'Да'), (False, 'Не')], default='Не', max_length=5),
        ),
    ]
