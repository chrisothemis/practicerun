from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

from filer.fields.image import FilerImageField


class PageFieldExtension(PageExtension):
    subtitle = models.CharField(max_length=255, blank=True)
    background_image = FilerImageField(null=True, blank=True)

extension_pool.register(PageFieldExtension)
