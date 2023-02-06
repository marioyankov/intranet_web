# Generated by Django 3.2 on 2023-02-06 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_request_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='cpu',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='drive',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='mac_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='ram',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='serial_number',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='computer',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.employee'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='video_card',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='cpu',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='drive',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='mac_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='serial_number',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.employee'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='video_card',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='wifi_mac_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='ports',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='serial_number',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.employee'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='drum',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.drum'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='mac_address',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='serial_number',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='printer',
            name='toner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.toner'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.employee'),
        ),
        migrations.AlterField(
            model_name='request',
            name='cartridge_name',
            field=models.CharField(choices=[('W1106A (106A)', 'W1106A (106A)'), ('CRG-724 H', 'CRG-724 H'), ('CRG-057 H', 'CRG-057 H'), ('CE285A', 'CE285A'), ('MLT-D204E', 'MLT-D204E'), ('4422810010', '4422810010'), ('CF217A', 'CF217A'), ('TK-130', 'TK-130'), ('953XL/957XL black', '953XL/957XL black'), ('CF410X Black', 'CF410X Black'), ('CF411X Cyan', 'CF411X Cyan'), ('CF412X Yellow', 'CF412X Yellow'), ('CF413X Magenta', 'CF413X Magenta'), ('LP-4240', 'LP-4240'), ('BTD60BK and BT5000M/C/Y', 'BTD60BK and BT5000M/C/Y'), ('TN-2421', 'TN-2421'), ('613511010', '613511010'), ('TK-1140', 'TK-1140'), ('CB436A', 'CB436A'), ('CRG-719', 'CRG-719'), ('CF226X', 'CF226X'), ('Q2612X', 'Q2612X'), ('613511015', '613511015'), ('CF283A', 'CF283A'), ('MLT-D2082L', 'MLT-D2082L'), ('MLT-D208L', 'MLT-D208L'), ('CE278A', 'CE278A'), ('TN-2120', 'TN-2120'), ('CB435A', 'CB435A'), ('CF256A', 'CF256A'), ('9004391', '9004391')], default='none', max_length=150),
        ),
        migrations.AlterField(
            model_name='request',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
