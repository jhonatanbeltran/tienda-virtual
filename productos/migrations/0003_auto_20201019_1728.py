# Generated by Django 3.1 on 2020-10-19 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20201016_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(upload_to='static/imgProductos'),
        ),
    ]
