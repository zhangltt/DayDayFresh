# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170531_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='upassword',
            field=models.CharField(max_length=40),
        ),
    ]
