# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodedata', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NodeData',
            new_name='RawNodeData',
        ),
    ]
