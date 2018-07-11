# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0006_auto_20180711_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trial',
            name='trialNumber',
        ),
        migrations.AddField(
            model_name='trial',
            name='trial_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
