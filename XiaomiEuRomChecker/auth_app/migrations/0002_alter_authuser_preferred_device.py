# Generated by Django 4.2.2 on 2023-07-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='preferred_device',
            field=models.CharField(blank=True, default='No Device', max_length=40, null=True),
        ),
    ]
