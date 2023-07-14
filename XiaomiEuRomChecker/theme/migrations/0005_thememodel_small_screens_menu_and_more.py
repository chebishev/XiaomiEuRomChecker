# Generated by Django 4.2.2 on 2023-07-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0004_remove_thememodel_theme_name_remove_thememodel_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='thememodel',
            name='small_screens_menu',
            field=models.CharField(choices=[('red', 'red'), ('pink', 'pink'), ('purple', 'purple'), ('deep-purple', 'deep-purple'), ('indigo', 'indigo'), ('blue', 'blue'), ('light-blue', 'light-blue'), ('cyan', 'cyan'), ('teal', 'teal'), ('green', 'green'), ('light-green', 'light-green'), ('lime', 'lime'), ('khaki', 'khaki'), ('yellow', 'yellow'), ('amber', 'amber'), ('orange', 'orange'), ('deep-orange', 'deep-orange'), ('blue-grey', 'blue-grey'), ('brown', 'brown'), ('light-grey', 'light-grey'), ('grey', 'grey'), ('dark-grey', 'dark-grey'), ('black', 'black')], default='red', max_length=20, verbose_name='Menu color on small screens'),
        ),
        migrations.AddField(
            model_name='thememodel',
            name='small_screens_menu_hover',
            field=models.CharField(choices=[('red', 'red'), ('pink', 'pink'), ('purple', 'purple'), ('deep-purple', 'deep-purple'), ('indigo', 'indigo'), ('blue', 'blue'), ('light-blue', 'light-blue'), ('cyan', 'cyan'), ('teal', 'teal'), ('green', 'green'), ('light-green', 'light-green'), ('lime', 'lime'), ('khaki', 'khaki'), ('yellow', 'yellow'), ('amber', 'amber'), ('orange', 'orange'), ('deep-orange', 'deep-orange'), ('blue-grey', 'blue-grey'), ('brown', 'brown'), ('light-grey', 'light-grey'), ('grey', 'grey'), ('dark-grey', 'dark-grey'), ('black', 'black')], default='white', max_length=20, verbose_name='Menu hover color on small screens'),
        ),
    ]
