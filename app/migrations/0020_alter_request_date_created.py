# Generated by Django 4.1.6 on 2023-02-04 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_request_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 4, 14, 24, 50, 555544, tzinfo=datetime.timezone.utc)),
        ),
    ]