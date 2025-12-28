from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()


# Create your models here.
class LinksModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="links")
    link_name = models.CharField(max_length=40, verbose_name="Link name")
    link_url = models.URLField(max_length=200, verbose_name="Link URL")
    link_description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    slug = models.SlugField(max_length=45, unique=True, editable=False, verbose_name="Slug")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.pk}-{self.link_name}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name_plural = "Links"
