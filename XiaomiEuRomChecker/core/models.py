from enum import Enum

from django.db import models
from django.template.defaultfilters import slugify


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.value) for choice in cls]


class ChoicesStringMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class RomOptions(ChoicesStringMixin, Enum):
    STABLE = 'stable'
    WEEKLY = 'weekly'
    BOTH = 'both'


# Create your models here.
class AvailableDevicesModel(models.Model):
    CODE_NAME_MAX_LENGTH = 20
    MARKET_NAME_MAX_LENGTH = 40
    ROM_NAME_MAX_LENGTH = 30
    code_name = models.CharField(max_length=CODE_NAME_MAX_LENGTH)
    market_name = models.CharField(max_length=MARKET_NAME_MAX_LENGTH, unique=True)
    rom_name = models.CharField(max_length=ROM_NAME_MAX_LENGTH)
    rom_options = models.CharField(
        max_length=RomOptions.max_length(),
        choices=RomOptions.choices(),
    )
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.market_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.market_name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Available Devices'


class FoldersModel(models.Model):
    folder_name = models.CharField(max_length=20, unique=True)
    last_modification_date = models.DateField()

    def __str__(self):
        return self.folder_name

    class Meta:
        verbose_name_plural = "Weekly Folders"
