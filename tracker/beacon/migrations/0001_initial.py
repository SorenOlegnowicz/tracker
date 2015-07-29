# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('child', models.ForeignKey(to='beacon.Child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=30)),
                ('child', models.ForeignKey(to='beacon.Child', related_name='child')),
                ('parent', models.ForeignKey(to='beacon.Parent')),
                ('pin', models.ForeignKey(to='beacon.Child', related_name='pin')),
            ],
        ),
        migrations.AddField(
            model_name='inquiry',
            name='parent',
            field=models.ForeignKey(to='beacon.Parent'),
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='pin',
            new_name='code',
        ),
    ]
