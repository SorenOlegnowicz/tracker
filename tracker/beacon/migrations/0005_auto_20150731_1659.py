# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0004_auto_20150730_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='child',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='code',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='parent',
        ),
        migrations.AddField(
            model_name='reply',
            name='inquiry',
            field=models.OneToOneField(default=1, to='beacon.Inquiry'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, default=1),
            preserve_default=False,
        ),
    ]
