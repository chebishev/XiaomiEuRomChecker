# Generated by Django 4.2.4 on 2023-08-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_threadtitle_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadtitle',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
