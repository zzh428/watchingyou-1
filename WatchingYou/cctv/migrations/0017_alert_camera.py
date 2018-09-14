# Generated by Django 2.1 on 2018-09-14 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cctv', '0016_alert'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='camera',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cctv.Camera', to_field='camera_id'),
        ),
    ]
