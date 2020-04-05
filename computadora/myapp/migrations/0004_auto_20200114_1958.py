# Generated by Django 2.2.3 on 2020-01-15 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200114_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleats',
            name='aire',
        ),
        migrations.RemoveField(
            model_name='detallelectups',
            name='aire',
        ),
        migrations.AddField(
            model_name='detalleats',
            name='Ats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Ats'),
        ),
        migrations.AddField(
            model_name='detallelectups',
            name='ups',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Ups'),
        ),
    ]
