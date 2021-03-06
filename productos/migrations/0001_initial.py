# Generated by Django 3.1 on 2020-10-16 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=20)),
                ('quienesSomos', models.TextField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcionCorta', models.CharField(max_length=250)),
                ('detalle', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('valor', models.DecimalField(decimal_places=1, max_digits=3)),
                ('keywords', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.marca')),
            ],
        ),
    ]
