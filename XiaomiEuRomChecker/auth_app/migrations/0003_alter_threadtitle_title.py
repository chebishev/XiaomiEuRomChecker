# Generated by Django 4.2.4 on 2023-08-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_threadtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threadtitle',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]