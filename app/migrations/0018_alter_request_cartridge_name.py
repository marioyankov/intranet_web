# Generated by Django 3.2 on 2023-01-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_request_cartridge_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='cartridge_name',
            field=models.CharField(choices=[('W1106A (106A)', 'W1106A (106A)'), ('CRG-724 H', 'CRG-724 H'), ('CRG-057 H', 'CRG-057 H'), ('CE285A', 'CE285A'), ('MLT-D204E', 'MLT-D204E'), ('CF217A', 'CF217A'), ('TK-130', 'TK-130')], default='none', max_length=150),
        ),
    ]