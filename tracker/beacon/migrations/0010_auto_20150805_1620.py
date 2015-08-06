# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0009_auto_20150805_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='id',
        ),
        migrations.AlterField(
            model_name='child',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='parent',
            name='telephone',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='inquiry',
            field=models.OneToOneField(serialize=False, to='beacon.Inquiry', primary_key=True),
        ),
    ]
