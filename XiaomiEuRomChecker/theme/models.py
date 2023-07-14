from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class ThemeModel(models.Model):
    OPTIONS = (
        ('red', 'red'),
        ('pink', 'pink'),
        ('purple', 'purple'),
        ('deep-purple', 'deep-purple'),
        ('indigo', 'indigo'),
        ('blue', 'blue'),
        ('light-blue', 'light-blue'),
        ('cyan', 'cyan'),
        ('teal', 'teal'),
        ('green', 'green'),
        ('light-green', 'light-green'),
        ('lime', 'lime'),
        ('khaki', 'khaki'),
        ('yellow', 'yellow'),
        ('amber', 'amber'),
        ('orange', 'orange'),
        ('deep-orange', 'deep-orange'),
        ('blue-grey', 'blue-grey'),
        ('brown', 'brown'),
        ('light-grey', 'light-grey'),
        ('grey', 'grey'),
        ('dark-grey', 'dark-grey'),
        ('black', 'black'),
    )
    navbar = models.CharField(max_length=20, choices=OPTIONS, default="red",
                              verbose_name="Navbar")
    navbar_hover = models.CharField(max_length=20, choices=OPTIONS, default="white",
                                    verbose_name="Navbar hover color")
    small_screens_navbar = models.CharField(max_length=20, choices=OPTIONS, default="white",
                                            verbose_name="Navbar on small screens")
    small_screens_menu = models.CharField(max_length=20, choices=OPTIONS, default="red",
                                          verbose_name="Menu color on small screens")
    small_screens_menu_hover = models.CharField(max_length=20, choices=OPTIONS, default="white",
                                                verbose_name="Menu hover color on small screens")
    header = models.CharField(max_length=20, choices=OPTIONS, default="red",
                              verbose_name="Header")
    first_grid_icon = models.CharField(max_length=20, choices=OPTIONS, default="red",
                                       verbose_name="First grid icon")
    second_grid_icon = models.CharField(max_length=20, choices=OPTIONS, default="red",
                                        verbose_name="Second grid icon")
    second_grid_background = models.CharField(max_length=20, choices=OPTIONS, default="light-grey",
                                              verbose_name="Second grid background")
    second_grid_p_color = models.CharField(max_length=20, choices=OPTIONS, default="grey",
                                           verbose_name="Second grid text color")
    rom_version_container = models.CharField(max_length=20, choices=OPTIONS, default="black",
                                             verbose_name="Rom version container")
    back_home_button = models.CharField(max_length=20, choices=OPTIONS, default="black",
                                        verbose_name="Back home button")

    def __str__(self):
        return "Color options"

    class Meta:
        verbose_name_plural = 'Themes'


class TipOfTheDayModel(models.Model):
    main_text = models.TextField(verbose_name="Main text")
    additional_text = models.TextField(verbose_name="Second text")

    def __str__(self):
        return "Tip of the day"

    class Meta:
        verbose_name_plural = 'Tip of the day'
