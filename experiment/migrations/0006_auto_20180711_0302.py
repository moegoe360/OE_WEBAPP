# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0005_auto_20180711_0253'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='trial',
            index_together=set([('table_name',)]),
        ),
    ]
