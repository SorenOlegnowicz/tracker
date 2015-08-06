# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0010_auto_20150805_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='replystamp',
            field=models.DurationField(null=True, blank=True),
        ),
    ]
