# Generated by Django 4.1.2 on 2022-12-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_employee_internet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d/'),
        ),
        migrations.AlterField(
            model_name='drum',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d/'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d/'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d/'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d/'),
        ),
        migrations.AlterField(
            model_name='toner',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y%m%d/'),
        ),
    ]