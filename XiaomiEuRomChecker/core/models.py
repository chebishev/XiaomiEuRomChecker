from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class AvailableDevicesModel(models.Model):
    code_name = models.CharField(max_length=20)
    market_name = models.CharField(max_length=40, unique=True)
    rom_name = models.CharField(max_length=30)
    rom_options = models.CharField(
        max_length=6,
        choices=[
            ('stable', 'stable'),
            ('weekly', 'weekly'),
            ('both', 'both'),
        ]
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
