# Generated by Django 2.2.3 on 2019-12-25 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='LugarReparacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procesador', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SistemaOperativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistema', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=60)),
                ('contrasena', models.CharField(max_length=25)),
                ('correo', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oficina', models.CharField(max_length=60)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=60)),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('fechacompra', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('observacion', models.CharField(max_length=100)),
                ('diagnosticada', models.CharField(max_length=60)),
                ('discoduro', models.CharField(max_length=60)),
                ('servicetag', models.CharField(max_length=60)),
                ('direccionip', models.CharField(max_length=60)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Estado')),
                ('lugar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.LugarReparacion')),
                ('modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Modelo')),
                ('oficina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Oficina')),
                ('procesador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Procesador')),
                ('sistema', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.SistemaOperativo')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('accion', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
