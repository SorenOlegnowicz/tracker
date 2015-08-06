# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import beacon.validators


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0008_auto_20150804_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='pin',
            field=models.CharField(max_length=4, validators=[beacon.validators.validate_pin, django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)]),
        ),

    ]
