from django.db import models


# Create your models here.
class AvailableDevicesModel(models.Model):
    code_name = models.CharField(max_length=20)
    market_name = models.CharField(max_length=40)
    rom_name = models.CharField(max_length=30)
    rom_options = models.CharField(
        max_length=6,
        choices=[
            ('stable', 'stable'),
            ('weekly', 'weekly'),
            ('both', 'both'),
        ]
    )

    class Meta:
        verbose_name_plural = 'Available Devices'
