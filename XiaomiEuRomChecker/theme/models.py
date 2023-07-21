from enum import Enum

from django.db import models


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.value) for choice in cls]


class ChoicesStringMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Color(ChoicesStringMixin, Enum):
    RED = 'red'
    PINK = 'pink'
    PURPLE = 'purple'
    DEEP_PURPLE = 'deep-purple'
    INDIGO = 'indigo'
    BLUE = 'blue'
    LIGHT_BLUE = 'light-blue'
    CYAN = 'cyan'
    TEAL = 'teal'
    GREEN = 'green'
    LIGHT_GREEN = 'light-green'
    LIME = 'lime'
    SAND = 'sand'
    KHAKI = 'khaki'
    YELLOW = 'yellow'
    AMBER = 'amber'
    ORANGE = 'orange'
    DEEP_ORANGE = 'deep-orange'
    BLUE_GREY = 'blue-grey'
    BROWN = 'brown'
    LIGHT_GREY = 'light-grey'
    GREY = 'grey'
    DARK_GREY = 'dark-grey'
    BLACK = 'black'
    WHITE = 'white'


# Create your models here.
class ThemeModel(models.Model):

    navbar = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="red",
                              verbose_name="Navbar")
    navbar_hover = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="white",
                                    verbose_name="Navbar hover color")
    small_screens_navbar = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="white",
                                            verbose_name="Navbar on small screens")
    small_screens_menu = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="red",
                                          verbose_name="Menu color on small screens")
    small_screens_menu_hover = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="white",
                                                verbose_name="Menu hover color on small screens")
    header = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="red",
                              verbose_name="Header")
    first_grid_icon = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="red",
                                       verbose_name="First grid icon")
    second_grid_icon = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="red",
                                        verbose_name="Second grid icon")
    second_grid_background = models.CharField(max_length=Color.max_length(), choices=Color.choices(),
                                              default="light-grey", verbose_name="Second grid background")
    second_grid_p_color = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="grey",
                                           verbose_name="Second grid text color")
    rom_version_container = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="black",
                                             verbose_name="Rom version container")
    back_home_button = models.CharField(max_length=Color.max_length(), choices=Color.choices(), default="black",
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
