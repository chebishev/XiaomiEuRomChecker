# Generated by Django 4.2.2 on 2023-06-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableDevicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=20)),
                ('market_name', models.CharField(max_length=40)),
                ('rom_name', models.CharField(max_length=30)),
                ('rom_options', models.CharField(choices=[('stable', 'stable'), ('weekly', 'weekly'), ('both', 'both')], max_length=6)),
            ],
        ),
    ]
