# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0008_trial_anon_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='query',
            field=models.CharField(max_length=1000),
        ),
    ]
