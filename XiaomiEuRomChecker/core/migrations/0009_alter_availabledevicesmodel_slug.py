# Generated by Django 4.2.2 on 2023-07-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_availabledevicesmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabledevicesmodel',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
