# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0007_auto_20150804_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=30)),
                ('position', geoposition.fields.GeopositionField(max_length=42)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='status',
            name='inquiry',
        ),
        migrations.RenameField(
            model_name='child',
            old_name='code',
            new_name='pin',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='position',
        ),
        migrations.RemoveField(
            model_name='inquiry',
            name='reply',
        ),
        migrations.AlterField(
            model_name='parent',
            name='first_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='last_name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='telephone',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='reply',
            name='inquiry',
            field=models.OneToOneField(to='beacon.Inquiry'),
        ),
    ]
