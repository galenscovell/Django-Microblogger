# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='favorites',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
