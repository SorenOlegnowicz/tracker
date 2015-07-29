# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(null=True, to='beacon.Parent'),
        ),
    ]
