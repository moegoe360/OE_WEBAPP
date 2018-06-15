# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='sql_table_creation',
            field=models.CharField(max_length=150, default=''),
            preserve_default=False,
        ),
    ]
