# Generated by Django 4.0 on 2021-12-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]