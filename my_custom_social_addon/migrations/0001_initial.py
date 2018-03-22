# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_pagenode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', related_name='my_custom_social_addon_social', parent_link=True, auto_created=True)),
                ('label', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SocialIcon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, to='cms.CMSPlugin', related_name='my_custom_social_addon_socialicon', parent_link=True, auto_created=True)),
                ('url_link', models.URLField()),
                ('link_title', models.CharField(blank=True, max_length=200)),
                ('extra_classes', models.CharField(blank=True, max_length=200)),
                ('icon', models.ForeignKey(to='my_custom_social_addon.Icon')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
