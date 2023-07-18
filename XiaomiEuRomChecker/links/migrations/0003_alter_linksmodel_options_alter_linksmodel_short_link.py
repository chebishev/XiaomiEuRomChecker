# Generated by Django 4.2.2 on 2023-07-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_linksmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linksmodel',
            options={'verbose_name_plural': 'Links'},
        ),
        migrations.AlterField(
            model_name='linksmodel',
            name='short_link',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Short link URL'),
        ),
    ]