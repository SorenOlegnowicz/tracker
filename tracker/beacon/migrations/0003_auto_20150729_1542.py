# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0002_child_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='first_name',
            field=models.CharField(max_length=20, default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='last_name',
            field=models.CharField(max_length=20, default='goodbye'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='telephone',
            field=models.CharField(max_length=20, default='1234567890'),
            preserve_default=False,
        ),
    ]
