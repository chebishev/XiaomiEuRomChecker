# Generated by Django 5.0 on 2024-01-08 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_threadtitle_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ThreadTitle',
        ),
    ]