# Generated by Django 4.1.2 on 2022-12-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_employee_internet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='internet',
            field=models.CharField(choices=[('Y', 'Да'), ('N', 'Не')], default='N', max_length=5),
        ),
    ]