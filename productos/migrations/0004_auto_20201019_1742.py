# Generated by Django 3.1 on 2020-10-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20201019_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
