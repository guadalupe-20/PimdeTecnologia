# Generated by Django 2.2.3 on 2020-03-22 00:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200321_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolo',
            name='hora',
            field=models.CharField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protocolo',
            name='lucessalida',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalleaire',
            name='horaaire',
            field=models.CharField(max_length=8),
        ),
    ]
