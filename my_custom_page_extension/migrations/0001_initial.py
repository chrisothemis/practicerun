# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0018_pagenode'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageFieldExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('background_image', filer.fields.image.FilerImageField(to=settings.FILER_IMAGE_MODEL, null=True, blank=True)),
                ('extended_object', models.OneToOneField(to='cms.Page', editable=False)),
                ('public_extension', models.OneToOneField(to='my_custom_page_extension.PageFieldExtension', related_name='draft_extension', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
