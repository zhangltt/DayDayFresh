# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170531_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='upostcode',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
