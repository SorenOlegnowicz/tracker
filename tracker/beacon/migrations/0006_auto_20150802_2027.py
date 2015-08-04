# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0005_auto_20150731_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='inquiry',
        ),
        migrations.AddField(
            model_name='inquiry',
            name='position',
            field=geoposition.fields.GeopositionField(default=(20, 20), max_length=42),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='reply',
            field=models.CharField(default='hey', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
