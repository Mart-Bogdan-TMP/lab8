# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxistation', '0002_remove_post_post_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
