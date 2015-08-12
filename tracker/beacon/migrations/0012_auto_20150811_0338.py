# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0011_inquiry_replystamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='relative_location',
            field=geoposition.fields.GeopositionField(default='0,0', max_length=42),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='position',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
    ]
