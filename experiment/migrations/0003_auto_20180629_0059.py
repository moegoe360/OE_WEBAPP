# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_experiment_sql_table_creation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='sql_table_creation',
            new_name='query',
        ),
    ]
