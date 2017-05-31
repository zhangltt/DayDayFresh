# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=30)),
                ('upasswod', models.CharField(max_length=30)),
                ('umail', models.CharField(max_length=30)),
                ('uconsignee', models.CharField(default=b'', max_length=30)),
                ('uaddress', models.CharField(default=b'', max_length=100)),
                ('upostcode', models.IntegerField(default=b'')),
                ('uphone', models.CharField(default=b'', max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
