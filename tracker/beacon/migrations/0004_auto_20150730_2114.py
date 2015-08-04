# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0003_auto_20150729_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='telephone',
            field=models.CharField(max_length=12, default='+14344651523'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parent',
            name='telephone',
            field=models.CharField(max_length=12),
        ),
    ]
