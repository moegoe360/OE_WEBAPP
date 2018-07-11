# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0004_auto_20180629_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trial',
            name='participant',
        ),
        migrations.AddField(
            model_name='trial',
            name='table_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
