# Generated by Django 4.2.2 on 2023-07-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_foldersmodel_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabledevicesmodel',
            name='slug',
            field=models.SlugField(default='mi-device', editable=False, unique=True),
        ),
    ]