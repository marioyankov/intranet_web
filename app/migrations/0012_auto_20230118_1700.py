# Generated by Django 3.2 on 2023-01-18 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20221214_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printer',
            name='drum',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.drum'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='toner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.toner'),
        ),
    ]