from django.db import models


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

    def __str__(self):
        return self.market_name

    class Meta:
        verbose_name_plural = 'Available Devices'


class FoldersModel(models.Model):
    folder_name = models.CharField(max_length=20, unique=True)
    last_modification_date = models.DateField()

    def __str__(self):
        return self.folder_name

    class Meta:
        verbose_name_plural = "Weekly Folders"
